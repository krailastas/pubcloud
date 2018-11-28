import json
import requests

from pubcloud.celery_app import app


@app.task
def send_to_cloud(data):
    try:
        serialized_data = json.dumps(data)
        requests.post(url='', data=serialized_data, headers={'Content-Type': 'application/json'})
    except Exception as exc:
        send_to_cloud.retry(exc=exc, countdown=300, max_retries=2)