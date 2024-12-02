set -o errexit

pip install -r requirements.txt

python AutoGo_proyecto/manage.py collectstatic --noinput
python AutoGo_proyecto/manage.py migrate