# 部署指南 (Deployment)

## 1. 数据库部署 (Supabase / Neon)
1. 运行 `db/init.sql` 初始化结构。
2. 确保开启 UUID 扩展：`CREATE EXTENSION IF NOT EXISTS "uuid-ossp";`

## 2. 后端部署 (FastAPI on Railway/Render)
1. 设置环境变量 `DATABASE_URL`。
2. 运行指令：`uvicorn main:app --host 0.0.0.0 --port $PORT`

## 3. 前端部署 (Next.js on Vercel)
1. 连接 GitHub 仓库。
2. 配置环境变量 `NEXT_PUBLIC_API_URL`。
3. 执行构建：`npm run build`。
