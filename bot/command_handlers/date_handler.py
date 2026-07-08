"""Import libraries"""
# Aiogram modules
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

# Other libraries
import logging
from datetime import datetime
from zoneinfo import ZoneInfo

"""Create router for date handler"""
date_router = Router()

"""Date handler"""
@date_router.message(Command("date"))
async def command_date_handler(message: Message) -> None:
    try:
        timezone_tehran = ZoneInfo("Asia/Tehran")
        now_tehran = datetime.now(timezone_tehran)
        formatted_now_tehran = now_tehran.strftime("%B %d, %Y at %I:%M %p")
        await message.reply(f"Tehran: {formatted_now_tehran}")
    except Exception as e:
        logging.error(f"Error in date handler: {e}")
        await message.reply("Sorry, couldn't process the /date")