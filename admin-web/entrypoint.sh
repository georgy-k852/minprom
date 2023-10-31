export APP_MODULE=${APP_MODULE-config.asgi:application}
export HOST=${HOST:-0.0.0.0}
export PORT=${PORT:-8000}
export BACKEND_CORS_ORIGINS=${BACKEND_CORS_ORIGINS}

python manage.py migrate
python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME
        --email=$DJANGO_SUPERUSER_EMAIL

#exec gunicorn --bind $HOST:$PORT "$APP_MODULE" -k uvicorn.workers.UvicornWorker
exec python manage.py runserver 0.0.0.0:8000