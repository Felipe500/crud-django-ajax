DIR_PROJECT_NAME=crud-django-ajax
BASE=/root/projects/demos/$DIR_PROJECT_NAME
ENV_FOLDER=venv

echo "### PROJECT 1 ###"
echo "ENTER FOLDER PROJECT"
cd $BASE && . $ENV_FOLDER/bin/activate

echo "### Pip install ###"
pip install -r requeriments-prod.txt

echo "### Django check ###"
python manage.py check --settings=config.settings.production

echo "### Migration ###"
python manage.py migrate --settings=config.settings.production

echo "### Sync with S3 ###"
python manage.py collectstatic --noinput
python manage.py collectstatic --noinput --settings=config.settings.production

echo  "### Restart gunicorn service and socket ###"
sudo systemctl restart app_crud_django.socket
sudo systemctl restart app_crud_django.service
sudo systemctl daemon-reload


echo "### Create symbolic link nginx config ###"
sudo ln -sfn /$BASE/nginx/app_crud_django.conf /etc/nginx/sites-enabled
if sudo nginx -t 2>&1 | grep -q 'successful'; then
    echo "### Reload Nginx ###"
    sudo /etc/init.d/nginx reload
else
    echo "### dir: $BASE ###"
    echo "Nginx Fail"
fi