#!/bin/bash

alembic upgrade head

# gunicorn "web:create_app()" --worker-class uvicorn.workers.UvicornWorker --chdir src/app/ --bind 0.0.0.0:8080 --workers 10
uvicorn web:create_app --factory --app-dir src/app/ --host=0.0.0.0 --port=8080 --reload