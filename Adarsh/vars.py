# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '23621595'))
    API_HASH = str(getenv('API_HASH', 'de904be2b4cd4efe2ea728ded17ca77d'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', ''))
    name = str(getenv('name', 'movieLover1_Bot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002277284028'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "1249672673").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'botmaster55'))

    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    else:
        ON_HEROKU = False

    FQDN = str(getenv('FQDN', 'https://resonant-rosie-bhaiforik76-6c00d401.koyeb.app/')) if not ON_HEROKU or getenv('FQDN') else APP_NAME + '.herokuapp.com'
    HAS_SSL = bool(getenv('HAS_SSL', False))

    if HAS_SSL:
        URL = "https://resonant-rosie-bhaiforik76-6c00d401.koyeb.app/".format(FQDN)
    else:
        URL = "https://resonant-rosie-bhaiforik76-6c00d401.koyeb.app/".format(FQDN)

    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://georgarevenio:8Gh0DpkI4K3RkVPA@cluster0.gyezl2s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'ClipMateBhai'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1002277284028")).split())) 
    SHORTLINK_URL = getenv('SHORTLINK_URL', '')
    SHORTLINK_API = getenv('SHORTLINK_API', '')
    TUTORIAL_URL = getenv('TUTORIAL_URL', '')
