from celery import Celery
from app.config import settings

celery_app = Celery(
    "tasks",
    broker=settings.RABBITMQ_URL,
    result_backend=settings.REDIS_URL,
    include=["app.tasks.process_request"]
)

celery_app.conf.task_routes = {
    "app.tasks.process_request.process_patient_request": {"queue": "requests"}
}