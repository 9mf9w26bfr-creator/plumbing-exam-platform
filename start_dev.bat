@echo off
echo ========================================================
echo Starting UK Plumbing Exam Platform (C&G 6035 / 8202)
echo ========================================================
echo.

echo Starting FastAPI Backend on http://localhost:8000 ...
start "Plumbing Exam Backend (FastAPI)" cmd /k "python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload"

echo Starting Next.js Frontend on http://localhost:3000 ...
cd frontend
start "Plumbing Exam Frontend (Next.js)" cmd /k "npm run dev"

echo.
echo Both servers are launching!
echo Backend API Docs: http://localhost:8000/docs
echo Web Platform:     http://localhost:3000
echo ========================================================
