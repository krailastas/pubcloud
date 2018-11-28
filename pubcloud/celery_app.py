from celery import Celery
from django.conf import settings

app = Celery('pubcloud')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
