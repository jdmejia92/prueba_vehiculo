#!/usr/bin/venv bash

set -o errexit

python -m venv venv
python3 venv/bin/activate
pip install -r requirements.txt

python AutoGo_proyecto/manage.py collecstatic --noinput
python AutoGo_proyecto/manage.py migrate