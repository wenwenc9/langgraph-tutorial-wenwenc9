import asyncio
import asyncpg
import sys
from typing import List, Optional
from pymilvus import connections, utility


async def clean_postgres_tables(connection: asyncpg.Connection) -> int:
    """
    清理 PostgreSQL 中的 LangGraph 相关表

    Args:
        connection: asyncpg 连接对象

    Returns:
        清理的表数量
    """
    print("🗑️  开始清理 PostgreSQL 表...")

    # LangGraph 相关表
    tables_to_clean = [
        'checkpoints',  # Checkpointer 主表
        'checkpoint_blobs',  # Checkpointer 大对象存储
        'checkpoint_writes',  # Checkpointer 写入记录
        'checkpoint_migrations',  # Checkpointer 迁移记录
        'store',  # Store 主表
        'store_migrations',  # Store 迁移记录
    ]

    cleaned_count = 0

    for table in tables_to_clean:
        try:
            # 检查表是否存在
            exists = await connection.fetchval(
                "SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = $1)",
                table
            )

            if exists:
                # 获取清理前的行数
                before_count = await connection.fetchval(f"SELECT COUNT(*) FROM {table}")

                if before_count > 0:
                    # 清理表数据
                    await connection.execute(f"TRUNCATE TABLE {table} CASCADE;")
                    print(f"  ✅ {table}: 已清理 {before_count} 行")
                    cleaned_count += 1
                else:
                    print(f"  ℹ️  {table}: 表为空,跳过")
            else:
                print(f"  ⚠️  {table}: 表不存在")

        except Exception as e:
            print(f"  ❌ {table}: 清理失败 - {str(e)}")

    return cleaned_count


def clean_milvus_collections(user_ids: Optional[List[str]] = None,
                             pattern: Optional[str] = None) -> int:
    """
    清理 Milvus Collections

    Args:
        user_ids: 指定用户ID列表,清理这些用户的 summary Collections
        pattern: Collection 名称模式(如 "summary_*")

    Returns:
        清理的 Collection 数量
    """
    print("🗑️  开始清理 Milvus Collections...")

    try:
        # 连接 Milvus
        connections.connect(
            alias="default",
            host=MILVUS_HOST,
            port=MILVUS_PORT,
            user=MILVUS_USER,
            password=MILVUS_PASSWORD
        )

        print(f"  🔗 已连接到 Milvus: {MILVUS_HOST}:{MILVUS_PORT}")

        # 获取所有 Collections
        all_collections = utility.list_collections()

        if not all_collections:
            print("  ℹ️  没有找到任何 Collections")
            return 0

        cleaned_count = 0

        # 确定要删除的 Collections
        collections_to_delete = []

        if user_ids:
            # 根据用户ID删除
            for user_id in user_ids:
                coll_name = f"summary_{user_id}"
                if coll_name in all_collections:
                    collections_to_delete.append(coll_name)
        elif pattern:
            # 根据模式匹配删除
            import fnmatch
            collections_to_delete = [
                coll for coll in all_collections
                if fnmatch.fnmatch(coll, pattern)
            ]
        else:
            # 删除所有 summary_ 开头的 Collections
            collections_to_delete = [
                coll for coll in all_collections
                if coll.startswith("summary_")
            ]

        if not collections_to_delete:
            print("  ℹ️  没有匹配的 Collections")
            return 0

        # 删除 Collections
        for coll_name in collections_to_delete:
            try:
                utility.drop_collection(coll_name)
                print(f"  ✅ {coll_name}: 已删除")
                cleaned_count += 1
            except Exception as e:
                print(f"  ❌ {coll_name}: 删除失败 - {str(e)}")

        return cleaned_count

    except Exception as e:
        print(f"  ❌ Milvus 清理失败: {str(e)}")
        return 0


async def quick_clean(
        clean_postgres: bool = True,
        clean_milvus: bool = True,
        user_ids: Optional[List[str]] = None
):
    """
    快速清理 LangGraph 相关数据

    Args:
        clean_postgres: 是否清理 PostgreSQL
        clean_milvus: 是否清理 Milvus
        user_ids: 指定用户ID列表(用于 Milvus)
    """
    print("=" * 60)
    print("🚀 开始快速清理 LangGraph 数据...")
    print("=" * 60)

    total_pg_tables = 0
    total_milvus_colls = 0

    # ==================== 清理 PostgreSQL ====================
    if clean_postgres:
        try:
            # 连接数据库
            connection = await asyncpg.connect(FULL_PG_URI)
            print(f"🔗 已连接到 PostgreSQL: {PG_DB_NAME}")

            try:
                total_pg_tables = await clean_postgres_tables(connection)
            finally:
                await connection.close()
                print("🔌 PostgreSQL 连接已关闭")

        except Exception as e:
            print(f"❌ PostgreSQL 清理失败: {str(e)}")

    # ==================== 清理 Milvus ====================
    if clean_milvus:
        try:
            total_milvus_colls = clean_milvus_collections(user_ids=user_ids)
        except Exception as e:
            print(f"❌ Milvus 清理失败: {str(e)}")

    # ==================== 汇总 ====================
    print("=" * 60)
    print("📊 清理汇总:")
    if clean_postgres:
        print(f"  PostgreSQL: {total_pg_tables} 个表")
    if clean_milvus:
        print(f"  Milvus: {total_milvus_colls} 个 Collections")
    print("=" * 60)

    if total_pg_tables > 0 or total_milvus_colls > 0:
        print("✅ 快速清理完成！")
    else:
        print("⚠️  没有清理任何数据")

    print("🎉 清理任务完成！")


# ==================== 命令行参数解析 ====================
def clean_main():

    # 执行清理
    asyncio.run(quick_clean(
        clean_postgres=True,
        clean_milvus=True,
        user_ids=None
    ))


if __name__ == "__main__":
    # ==================== 配置(直接硬编码) ====================
    PG_URI = "postgresql://postgres:123456@localhost:5432/wenwenc9"
    PG_DB_NAME = "langgraph-learn"
    FULL_PG_URI = f"postgresql://postgres:123456@localhost:5432/{PG_DB_NAME}"

    MILVUS_HOST = "localhost"
    MILVUS_PORT = "19530"
    MILVUS_USER = "root"
    MILVUS_PASSWORD = "Milvus123456-123456789"

    clean_main()