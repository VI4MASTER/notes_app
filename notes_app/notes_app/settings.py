"""
Налаштування Django для проєкту notes_app.

Створено за допомогою 'django-admin startproject' з використанням Django 5.2rc1.

Для додаткової інформації про цей файл див.:
https://docs.djangoproject.com/en/dev/topics/settings/

Для повного списку налаштувань та їх значень див.:
https://docs.djangoproject.com/en/dev/ref/settings/
"""

from pathlib import Path

# Створення шляхів у проєкті, наприклад: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Налаштування для швидкого старту розробки - не підходять для продакшену
# Див. https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# ПОПЕРЕДЖЕННЯ БЕЗПЕКИ: тримайте секретний ключ у продакшені в таємниці!
SECRET_KEY = 'django-insecure-5gth)g0$1+^bbp_te+=s+raj$1hz9xquj2es8)(fhqzc=wn91b'

# ПОПЕРЕДЖЕННЯ БЕЗПЕКИ: не запускайте з увімкненим дебагом у продакшені!
DEBUG = True

ALLOWED_HOSTS = []


# Визначення додатків

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'notes',  # Додано додаток notes
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'notes_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'notes_app.wsgi.application'


# База даних
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Валідатори паролів
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Інтернаціоналізація
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'uk-ua'

TIME_ZONE = 'Europe/Kyiv'

USE_I18N = True

USE_TZ = True


# Статичні файли (CSS, JavaScript, зображення)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Тип поля первинного ключа за замовчуванням
# https://docs.djangoproject.com/en/dev/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'