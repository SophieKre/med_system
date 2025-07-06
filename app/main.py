from fastapi import FastAPI
from app.api.patients import router as patients_router
from app.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(patients_router, prefix="/api/v1")

@app.get("/health")
def health_check():
    return {"status": "ok"}