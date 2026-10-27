# 部署指南 (Deployment Guide)

## 1. GitHub 倉庫
本專案已成功推播至 GitHub：
- **倉庫地址**: [https://github.com/9mf9w26bfr-creator/plumbing-exam-platform](https://github.com/9mf9w26bfr-creator/plumbing-exam-platform)
- **默認分支**: `main`

---

## 2. 前端部署 (Next.js on Vercel)

本專案已內建完整的 Vercel 部署設定與雙模架構（可開箱即用作為 Vercel Serverless 全功能運行，亦可對接外部 FastAPI 後端）：

### 方法 A：Vercel 網頁控制台一鍵導入（最推薦）
1. 登入 [Vercel Dashboard](https://vercel.com/new)。
2. 在 **Import Git Repository** 中找到或搜尋 `plumbing-exam-platform`。
3. 點選 **Import**。
4. 設定確認：
   - **Framework Preset**: `Next.js`（自動識別）
   - **Root Directory**: 默認即可（專案已配置根目錄與 `frontend` 的 `vercel.json` 智慧導向）
   - **Build Command**: 自動運行 `npm run build`
5. 點擊 **Deploy**，約 1~2 分鐘即可完成部署並獲得正式的 `https://plumbing-exam-platform.vercel.app` 網址！

### 方法 B：Vercel CLI 終端指令部署
在專案根目錄或 `frontend` 目錄下執行：
```bash
vercel login
vercel --prod
```

> **提示**：若使用外部獨立後端，只需在 Vercel 專案設定中加入環境變數 `NEXT_PUBLIC_API_URL=https://your-api-domain.com/api` 即可無縫切換。

---

## 3. 後端與資料庫獨立部署 (選配：Railway / Render + Supabase / Neon)
如需獨立託管 Python FastAPI 高併發後端服務與雲端 PostgreSQL：
1. **資料庫 (Supabase/Neon)**：建立 PostgreSQL 例項，複製連線字串。
2. **後端 (Railway/Render)**：
   - 連結 GitHub 倉庫。
   - 根目錄設定為 `backend` 或執行命令：`python -m uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
   - 設定環境變數 `DATABASE_URL`。

