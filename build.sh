set -o errexit

pip install -r requirements.txt

cd AutoGo_proyecto

python manage.py collectstatic --noinput
python manage.py migrate