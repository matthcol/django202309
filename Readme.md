# Django Project

## Install

```
pip install Django
pip install django-extensions
pip install psycopg
python -m django --version
```

## Create Project 

django-admin startproject movies

## Create App

python manage.py startapp movieapp

## Create Model and DB

python manage.py makemigrations movieapp
python manage.py sqlmigrate movieapp 0001
python manage.py migrate --dry-run
python manage.py migrate
python manage.py migrate movieapp 0003
python manage.py migrate movieapp zero
python manage.py showmigrations 
python manage.py showmigrations movieapp

## Use Notebook to test ORM
Set environment variable DJANGO_ALLOW_ASYNC_UNSAFE

### Command Dos
```
set DJANGO_ALLOW_ASYNC_UNSAFE=True
```

### Powershell
```
${env:DJANGO_ALLOW_ASYNC_UNSAFE}="True"
```

### Bash
```
export DJANGO_ALLOW_ASYNC_UNSAFE=True
```
