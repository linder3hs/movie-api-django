# Pasos para deploy

## 1. Instalamos dependencias

```bash
pip install gunicorn

pip install django-environ

pip install mysqlclient

pip install whitenoise
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
MYSQLDATABASE=
MYSQLUSER=
MYSQLPASSWORD=
MYSQLHOST=
MYSQLPORT=
```

## 6. Configuramos nuestro dominio

Para que el proyecto pueda ser accedido desde un dominio, debemos configurar el dominio en railway y en nuestro proyecto.

```py
ALLOWED_HOSTS = ['domain.railway.app']

CSRF_TRUSTED_ORIGINS = ['https://domain.railway.app']

```

## 7. Configuramos nuestros archivos staticos

```py
INSTALLED_APPS = [
    ...,
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',    
    ...
]

MIDDLEWARE = [
    ...,
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    ...
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE="whitenoise.storage.CompressedManifestStaticFilesStorage"
```
