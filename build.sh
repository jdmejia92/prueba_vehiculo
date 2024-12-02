set -o errexit

pip install -r requirements.txt

python AutoGo_proyecto/manage.py collectstatic --noinput

cd AutoGo_proyecto/AutoGo/
python AutoGo_proyecto/manage.py migrate