

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--9_a69zlgkso3)i)j68%bg=we@qc88j-c13ga55*zzdmqa@-8#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',
    'relationship_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'bookshelf.middleware.CSPHeaderMiddleware',
]

ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'LibraryProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



AUTH_USER_MODEL = 'bookshelf.CustomUser'  # set the AUTH_USER_MODEL to point to your new custom user model.
MEDIA_URL = '/media/'  
MEDIA_ROOT = BASE_DIR / 'media'




# Browser-side protections  
SECURE_BROWSER_XSS_FILTER = True  
X_FRAME_OPTIONS = 'DENY'  
SECURE_CONTENT_TYPE_NOSNIFF = True  

# Secure cookies  
CSRF_COOKIE_SECURE = True  # Cookies are sent over HTTPS only  
SESSION_COOKIE_SECURE = True  # Session cookies are sent over HTTPS only  

# settings.py  

# Enable HTTPS redirection  
SECURE_SSL_REDIRECT = True  # Redirect all non-HTTPS requests to HTTPS  

# HTTP Strict Transport Security (HSTS) settings  
SECURE_HSTS_SECONDS = 31536000  # Enforce HTTPS for one year  
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Include all subdomains in HSTS policy  
SECURE_HSTS_PRELOAD = True  # Allow preloading of HSTS  

# Secure cookie settings  
SESSION_COOKIE_SECURE = True  # Ensure session cookies are only sent over HTTPS  
CSRF_COOKIE_SECURE = True  # Ensure CSRF cookies are only sent over HTTPS  

# Implement secure headers  
X_FRAME_OPTIONS = 'DENY'  # Prevent clickjacking by denying framing  
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent MIME-sniffing  
SECURE_BROWSER_XSS_FILTER = True  # Enable XSS filtering in browsers

SECURE_PROXY_SSL_HEADER = True
HTTP_X_FORWARDED_PROTO = True