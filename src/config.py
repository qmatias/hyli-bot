

from dotenv import load_dotenv
from pathlib import Path
import os
from typing import Optional, Union
import re


load_dotenv()

ROOT_DIR = Path(__file__).resolve().parent
MEDIA_PATH = ROOT_DIR / 'media'

PETPET_TEMPLATE = MEDIA_PATH / 'template.png'
GAY1 = MEDIA_PATH / 'gay1.jpg'
GAY2 = MEDIA_PATH / 'gay2.jpg'
HORNY = MEDIA_PATH / 'horny.gif'
BANGER = MEDIA_PATH / 'banger.png'
AWESOME = MEDIA_PATH / 'awesome.png'
HUSH = MEDIA_PATH / 'hush.png'
MAD = MEDIA_PATH / 'mad.png'
NERD = MEDIA_PATH / 'nerd.png'
SINGLE = MEDIA_PATH / 'single.png'
CAMEL = MEDIA_PATH / 'camel.png'
ASS = MEDIA_PATH / 'ass.png'

AMOGUS = MEDIA_PATH / 'amogus.mp3'
YEAH = MEDIA_PATH / 'yeah.mp3'

FATHER_SONG_PATH = MEDIA_PATH / 'fatheroflies.txt'
ASTRONAUT_SONG_PATH = MEDIA_PATH / 'astronaut.txt'
SHUTUP_PATH = MEDIA_PATH / 'shutup'

HH_SERVER = 401575621819367425
TEST_SERVER = 523240131482877970

BOT_TOKEN = os.getenv("BOT_TOKEN")
if BOT_TOKEN is None:
    raise ValueError('Need a discord BOT_TOKEN')

DATABASE_URL = os.getenv('DATABASE_URL')
if DATABASE_URL is None:
    raise ValueError('Need a DATABASE_URL')

TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
if TWITTER_API_KEY is None:
    raise ValueError('Need a TWITTER_API_KEY')

TWITTER_API_KEY_SECRET = os.getenv('TWITTER_API_KEY_SECRET')
if TWITTER_API_KEY_SECRET is None:
    raise ValueError('Need a TWITTER_API_KEY_SECRET')

TWITTER_BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')
if TWITTER_BEARER_TOKEN is None:
    raise ValueError('Need a TWITTER_BEARER_TOKEN')

TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
if TWITTER_ACCESS_TOKEN is None:
    raise ValueError('Need a TWITTER_ACCESS_TOKEN')

TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
if TWITTER_ACCESS_TOKEN_SECRET is None:
    raise ValueError('Need a TWITTER_ACCESS_TOKEN_SECRET')

# discord command prefix
PREFIX = '!'

# uwu channel
UWU_PATTERN = re.compile(r'^(|.*[^a-z])(uwu|owo)(|[^a-z].*)$', re.IGNORECASE)

# quotes channel
QUOTES_PATTERN = re.compile(r'^[^a-z]*quotes?[^a-z]*$', re.IGNORECASE)

# reactions
# REACTION_YES = '✅'
# REACTION_NO = '❌'

LFTP = 333707773332291605
LFTP_TRUSTED_ROLE = 618937559996956678

ABHISHEK = 315898478712717312
VIOLET = 382674822926434335
MATIAS = 224292077868023809
RAGHAV = 229713250793553922
ZAPATA = 180439899567030272
LUKE = 160524407016521728
KEVIN = 169935204096409600

LEAGUE_ROLE = 554831644557705236
LEAGUE_GIF = 'https://tenor.com/view/squidward-spare-some-change-beggar-gif-13086110'


# messages
SEND_ERROR = 'The message is too long'
NO_PERMISSIONS = 'This bot is missing permissions to do that'
MESSAGE_TIMER = 3
