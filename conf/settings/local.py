from .base import *

DEBUG = True

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, Javascript, Images)
STATIC_URL = '/assets/'
STATIC_ROOT = os.path.join(BASE_DIR, 'assets/')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'conf', 'static'),
    os.path.join(BASE_DIR, 'golf', 'static'),
]
