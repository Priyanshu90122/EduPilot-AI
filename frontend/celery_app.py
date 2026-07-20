"""Celery application instance. Run worker with: celery -A app.celery_app worker -l info"""
from celery import Celery

from app.core.config import settings

celery_app = Celery(
    "edupilot",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
    include=["app.tasks.document_tasks", "app.tasks.reminder_tasks"],
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="Asia/Kolkata",
    enable_utc=True,
    task_track_started=True,
    task_time_limit=600,
    beat_schedule={
        "check-deadline-reminders-every-hour": {
            "task": "app.tasks.reminder_tasks.check_upcoming_deadlines",
            "schedule": 3600.0,
        },
    },
)
