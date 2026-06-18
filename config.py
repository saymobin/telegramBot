"""Import libraries"""
# Other libraries
from dotenv import load_dotenv
from os import getenv

"""Load variables"""
load_dotenv()

TOKEN = getenv("BOT_TOKEN1")
if not TOKEN:
    raise ValueError("BOT_TOKEN1 is not set in .env")
PROXY = getenv("PROXY")
DATE_STATUS = getenv("DATE_STATUS")
ECHO_STATUS = getenv("ECHO_STATUS")