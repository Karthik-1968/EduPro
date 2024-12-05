# edupro


## setup virtualenv

```sh
pip install virtualenv
virtualenv .venv
```

## install requirements

```bash
pip install -r requirements_project.txt
pip install -r requirements_test.txt
```

## running django management commands & usage

```sh
source .venv/bin/activate
export DJANGO_SETTINGS_MODULE=edupro.settings.local
python manage.py build -a edu_core
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```


### setup python3.10 
chmod +x setup_python3.10.sh
./setup_python3.10.sh