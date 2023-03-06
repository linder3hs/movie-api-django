# Pasos para deploy

## 1. Instalamos dependencias

```bash
pip install gunicorn

pip install django-environ
```

## 2. Creamos nuestro requirements

```bash
pip freeze > requirements.txt
```

## 3. Creamos nuestro Procfile

```bash
web: python manage.py migrate && gunicorn movies.wsgi
```

## 4. Creamos nuestra base de datos en railway

Estamos usando mysql por defecto.

[railway.app](https://railway.app/)

## 5. Configuramos las variables de nuestro proyecto

```python
DB_NAME=''
DB_USER=''
DB_PASSWORD=''
DB_HOST=''
DB_PORT=''
```
