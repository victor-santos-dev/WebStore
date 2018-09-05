web: newrelic-admin run-program gunicorn webStore.wsgi --log-file -
celery: celery worker -A webStore -l info
