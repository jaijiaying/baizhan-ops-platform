# 阶段09｜百战智能运营平台（学习复现）

依据已登录课程 65476、65477 的视频画面和章节文档整理的独立复现骨架，不是课程源码。

## 产品链路
热搜检索/主题灵感 → 标题与小红书文案 → 敏感词检查 → 封面和正文图片 → OSS 存储 → 多账号发布 → 历史记录与素材库。

## 课程确认的技术选型
Python 3.12、FastAPI/Uvicorn、MySQL 8、Tortoise ORM、Aerich、JWT、Coze、Dashscope、python-multipart、阿里云 OSS、Postman。

## 当前状态
已建立项目目录、领域模块清单和接口边界；继续读取课程 65478–65551 后，将按视频实际代码和画面补齐实现。

## 已读取课程 65479｜项目搭建_初始化项目（07:43）

视频画面实际显示：创建 `operation` 文件夹，用 Cursor 打开项目，安装 uv，运行 `uv init`，再安装 FastAPI、Uvicorn、Tortoise ORM、Aerich、JWT、Coze、Dashscope、OSS 等依赖。

文档步骤：复制 `.env.example` 为 `.env`，填写 MySQL 连接；创建 `app/config.py` 组装 `DATABASE_URL` 与 `TORTOISE_ORM`；创建模型文件；运行 `uv run aerich init -t app.config.TORTOISE_ORM` 和 `uv run aerich init-db`，生成 Aerich 表表示数据库连接成功。

## 已读取课程 65480｜项目搭建_配置文件（08:54）

视频画面实际显示 Cursor 中的 `.env` 文件：`DB_HOST=localhost`、`DB_PORT=3306`、`DB_USER=root`、`DB_PASSWORD=root`、`DB_NAME=baizhan_operation`。这些值用于连接上一节创建的 MySQL 数据库。

## 已读取课程 65481｜项目搭建_模型文件（07:09）

视频画面实际显示在 `app/models/__init__.py` 中从 `tortoise` 导入 `fields` 和 `Model`，并开始定义 `User`、`Section` 等模型；`User` 映射 `t_users`，包含 username、password、name、department、created_at 等字段。完整表字段与课程 65478 文档一致，本地已补充前三个核心模型骨架。
