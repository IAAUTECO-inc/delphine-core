import os
import logging

# NIS2 Compliance Settings
# ========================

# 1. Secret Management
SECRET_KEY = os.environ.get('KOALIXCRM_SECRET_KEY')
if not SECRET_KEY:
    # In a real production app, we might raise an error, but for dev/demo we warn.
    # raise ValueError("KOALIXCRM_SECRET_KEY environment variable is not set.")
    pass

# 2. Debug Mode
DEBUG = os.environ.get('KOALIXCRM_DEBUG', 'False') == 'True'

# 3. Firebase Configuration
FIREBASE_CREDENTIALS_PATH = os.environ.get('FIREBASE_CREDENTIALS_PATH', 'firebase-credentials.json')
FIREBASE_DATABASE_URL = os.environ.get('FIREBASE_DATABASE_URL')  # Optional for Realtime Database
# For Firestore, credentials file is sufficient

# 4. Logging and Auditing
LOG_LEVEL = logging.INFO if not DEBUG else logging.DEBUG
LOG_FILE = 'security.log'

logging.basicConfig(
    level=LOG_LEVEL,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_FILE)
    ]
)

def get_logger(name):
    return logging.getLogger(name)
