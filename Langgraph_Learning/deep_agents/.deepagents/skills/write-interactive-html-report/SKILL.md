---
name: write-interactive-html-report
description: 生成包含个人信息的交互式HTML报告-2
triggers:
  - HTML报告
  - 生成网页
  - 可视化报告
  - 个人信息展示
---

# 个人信息HTML报告生成技能

## 目标
根据查询到的个人信息数据，生成一个美观、交互式的HTML报告。

## 报告要求

### 1. 页面结构
- 使用HTML5语义化标签
- 响应式设计，支持移动端查看
- 包含页面标题和生成时间

### 2. 样式设计
- 使用卡片式布局展示每个人的信息
- 使用渐变色或现代化配色方案，红色
- 添加悬停效果和过渡动画
- 使用图标美化信息展示

### 3. 内容展示
每个人员卡片应包含：
- 头像/emoji
- 基本信息：姓名、年龄、性别、城市
- 职业信息：职位、公司、薪资
- 教育背景
- 技能标签（使用标签云样式）
- 兴趣爱好
- 项目经验

### 4. 交互功能
- 搜索/筛选功能（可选）
- 点击卡片展开详细信息
- 数据统计图表（如年龄分布、技能分布等）

## HTML模板示例

<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>个人信息汇总报告</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            min-height: 100vh;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        h1 {
            text-align: center;
            color: white;
            margin-bottom: 30px;
            font-size: 2.5em;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        .cards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 25px;
            margin-top: 30px;
        }
        .card {
            background: white;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 40px rgba(0,0,0,0.4);
        }
        .card-header {
            display: flex;
            align-items: center;
            margin-bottom: 20px;
            border-bottom: 2px solid #667eea;
            padding-bottom: 15px;
        }
        .avatar {
            font-size: 3em;
            margin-right: 15px;
        }
        .name {
            font-size: 1.8em;
            font-weight: bold;
            color: #333;
        }
        .info-row {
            margin: 10px 0;
            display: flex;
            align-items: center;
        }
        .info-label {
            font-weight: bold;
            color: #667eea;
            min-width: 80px;
        }
        .skills {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 10px;
        }
        .skill-tag {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.85em;
        }
        .footer {
            text-align: center;
            color: white;
            margin-top: 40px;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>👥 个人信息汇总报告</h1>
        
        <div class="cards-grid">
            <!-- 这里插入每个人的卡片 -->
            <div class="card">
                <div class="card-header">
                    <div class="avatar">👨‍💻</div>
                    <div class="name">张伟</div>
                </div>
                <div class="info-row">
                    <span class="info-label">年龄：</span>
                    <span>28岁</span>
                </div>
                <!-- 更多信息... -->
                <div class="skills">
                    <span class="skill-tag">Python</span>
                    <span class="skill-tag">Java</span>
                </div>
            </div>
        </div>
        
        <div class="footer">
            <p>报告生成时间：2026-01-22</p>
        </div>
    </div>
</body>
</html>
\```

## 使用步骤

1. 收集所有通过 `query_personal_infos` 获取的数据
2. 为每个人创建一个卡片HTML片段
3. 将所有卡片插入到模板的 `.cards-grid` 中
4. 使用 `write_file` 工具保存为 `personal_report.html`
5. 告知用户文件已生成，可以在浏览器中打开查看