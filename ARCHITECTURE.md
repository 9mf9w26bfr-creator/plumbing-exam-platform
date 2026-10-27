# 网站技术架构 (Architecture)

## 1. 核心技术栈
*   **前端 (Frontend)**: Next.js (React), TypeScript, Tailwind CSS
*   **后端 (Backend)**: FastAPI (Python), Pydantic (数据校验)
*   **数据库 (Database)**: PostgreSQL (通过 SQLAlchemy 或 SQLModel ORM 交互)
*   **部署 (Deployment)**: Vercel (前端), Railway/Render (后端), Supabase/Neon (数据库)

## 2. 架构设计
*   **前后端分离**: Next.js 仅负责 UI 渲染和状态管理 (Zustand/Redux)；FastAPI 负责核心业务逻辑与题库检索。
*   **双轨索引架构**: 
    后端 API 提供 `/api/questions/by-chapter/{chapter_id}` 和 `/api/questions/by-unit/{unit_id}` 两个主要获取题目的接口。
*   **状态切换**: 前端实现全局上下文 (Context) 来即时切换中/英双语显示，只需读取同一个 JSON 对象的 `content_en` 或 `content_zh` 字段。
