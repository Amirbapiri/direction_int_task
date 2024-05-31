import os
from django.conf import settings
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "direction_api.settings.local")

app = Celery("direction_api")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    "run-scrapy-spider-every-30-minutes": {
        "task": "job_scraper.tasks.run_spider",
        "schedule": 1800.0,
    }
}
