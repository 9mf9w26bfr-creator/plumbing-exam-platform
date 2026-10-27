from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.database import engine, Base
from backend.app.routers import chapters, units, questions, cms
from backend.app.seed_data import seed_database

# Create DB tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Plumbing Exam Mock Platform API",
    description="Dual-track City & Guilds Plumbing Level 2/3 Mock Exam & Practice Platform complying with Project Constitution",
    version="1.0.0"
)

# CORS setup for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(chapters.router)
app.include_router(units.router)
app.include_router(questions.router)
app.include_router(cms.router)


@app.on_event("startup")
def on_startup():
    # Automatically seed default chapters, units, and verified questions if empty
    seed_database()


@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "system": "Plumbing Exam Platform API",
        "compliance": "City & Guilds 6035/8202 Constitution Compliant"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
