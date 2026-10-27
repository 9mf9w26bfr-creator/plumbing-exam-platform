Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "Starting UK Plumbing Exam Platform (C&G 6035 / 8202)" -ForegroundColor Cyan
Write-Host "========================================================" -ForegroundColor Cyan

# Start Backend
Start-Process powershell -ArgumentList "-NoExit", "-Command", "python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload"

# Start Frontend
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd frontend; npm run dev"

Write-Host "Backend API Docs: http://localhost:8000/docs" -ForegroundColor Green
Write-Host "Web Platform:     http://localhost:3000" -ForegroundColor Green
