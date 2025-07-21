from celery import Celery
# from app.config import settings
import os
# celery_app = Celery(
#     "tasks",
#     broker=settings.RABBITMQ_URL,
#     result_backend=settings.REDIS_URL,
#     include=["app.tasks.process_request"]
# )

# celery_app.conf.task_routes = {
#     "app.tasks.process_request.process_patient_request": {"queue": "requests"}
# }


celery_app = Celery(
    "medical_triage",
    broker=os.getenv("CELERY_BROKER", "redis://localhost:6379/0"),
    backend=os.getenv("CELERY_BACKEND", "redis://localhost:6379/0")
)

celery_app.conf.task_routes = {
    "app.tasks.analyze_symptoms": {"queue": "requests"}
}
