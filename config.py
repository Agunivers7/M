import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("API_ID", "10651048"))
API_HASH = getenv("API_HASH","37775aca7d11f450ecde375baac17fe7")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN","5475804553:AAEomjFZJy7_NECHqe67rdp0qUSr_enBgmw")
