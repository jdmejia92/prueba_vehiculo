#!/usr/bin/venv bash

set -o errexit

pip install -r requirements.txt

python AutoGo_proyecto/manage.py collecstatic --noinput
python AutoGo_proyecto/manage.py migrate