
# 一、项目说明

![img.png](static/img.png)

配合博客文章讲解，点击专栏，langgraph，跟着系列文章运行响应代码即可
https://blog.csdn.net/weixin_44238683


**Langgraph系列文章**
- [01｜Langgraph | 从入门到实战 | 基础篇](https://blog.csdn.net/weixin_44238683/article/details/153200305)
- [02｜Langgraph | 从入门到实战 | workflow与Agent](https://blog.csdn.net/weixin_44238683/article/details/154188541)
- [03｜Langgraph | 从入门到实战 | 进阶篇 | 持久化](https://blog.csdn.net/weixin_44238683/article/details/154648157)
- [04｜Langgraph | 从入门到实战 | 进阶篇 | 流式传输](https://blog.csdn.net/weixin_44238683/article/details/156984982)
- [05｜Langgraph | 从入门到实战 | 进阶篇 | 中断interrupt](https://blog.csdn.net/weixin_44238683/article/details/157176498)

**langchain的系列文章（相信我把Langchain全部学一遍，你能深入理解AI的开发）**
- [01｜LangChain | 从入门到实战-介绍](https://blog.csdn.net/weixin_44238683/article/details/134217850)
- [02｜LangChain | 从入门到实战 -六大组件之Models IO](https://blog.csdn.net/weixin_44238683/article/details/134219526)
- [03｜LangChain | 从入门到实战 -六大组件之Retrival](https://blog.csdn.net/weixin_44238683/article/details/137914108)
- [04｜LangChain | 从入门到实战 -六大组件之Chain](https://blog.csdn.net/weixin_44238683/article/details/137924938)
- [05｜LangChain | 从入门到实战 -六大组件之Memory](https://blog.csdn.net/weixin_44238683/article/details/138178023)
- [06｜LangChain | 从入门到实战 -六大组件之Agent](https://blog.csdn.net/weixin_44238683/article/details/138276724)
# 二、环境设置

1、安装UV
```bash
pip install uv
```

2、创建python环境
```bash
uv venv --python=3.13
```

3、激活虚拟环境
```bash
.venv\Scripts\activate
```

4、安装包 【使用清华源】
```bash
uv  sync  -i https://pypi.tuna.tsinghua.edu.cn/simple
```

5、复制[.env.example](.env.example)为.evn并且配置key为你自己的