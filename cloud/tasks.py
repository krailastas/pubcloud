from django.conf import settings
from google.cloud import pubsub_v1

from pubcloud.celery_app import app


@app.task
def send_to_cloud(data):
    try:
        publisher = pubsub_v1.PublisherClient()
        topic_path = publisher.topic_path(settings.GOOGLE_PROJECT_ID, settings.GOOGLE_TOPIC_ID)
        data = u'{}'.format(data['message'])
        data = data.encode('utf-8')
        publisher.publish(topic_path, data=data)
    except Exception as exc:
        send_to_cloud.retry(exc=exc, countdown=300, max_retries=2)