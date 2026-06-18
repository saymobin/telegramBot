# Other libraries
from dotenv import load_dotenv
from os import getenv

"""Config variables"""
load_dotenv()

DATE_STATUS = getenv("DATE_STATUS")
TOKEN = getenv("BOT_TOKEN1")
if not TOKEN:
    raise ValueError("BOT_TOKEN1 is not set in .env")
PROXY = getenv("PROXY")