import os
import dj_database_url
from pathlib import Path

# 1. Configuración de rutas
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Carga de variables (busca .env localmente, pero en Render usa las del Panel)
load_dotenv(os.path.join(BASE_DIR, '.env'))

# 3. Puente para MySQL
pymysql.install_as_MySQLdb()

# --- SEGURIDAD Y ENTORNO ---
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-z!x9m2f8n^v1q5p0l+a3c8e4j7b6r9w1v5t0y4u2i7o8p3k')
DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True' 
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', 'localhost 127.0.0.1').split()

# --- BASE DE DATOS (Centralizada y Única) ---
# Usamos dj_database_url para parsear la variable DATABASE_URL de Aiven
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=False  # Aiven suele manejar el SSL por fuera, esto evita conflictos
    )
}

if 'RENDER' in os.environ:
    DATABASES['default']['OPTIONS'] = {
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        # Esto elimina parámetros conflictivos de la conexión
    }
# --- APLICACIONES ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'contacto',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'corexandes_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'contacto' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'corexandes_site.wsgi.application'

AUTH_PASSWORD_VALIDATORS = []
LANGUAGE_CODE = 'es-cl'
TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_TZ = True

# --- ARCHIVOS ESTÁTICOS (Render/WhiteNoise) ---
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'contacto', 'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- EMAIL (Zoho) ---
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.zoho.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'True') == 'True'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', 'tu-email@dominio.cl')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', 'tu-password')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER