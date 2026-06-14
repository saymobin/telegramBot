"""Import libraries"""
# Aiogram modules
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.client.session.aiohttp import AiohttpSession

# Other libraries
import asyncio
import logging
from os import getenv
from datetime import datetime
from zoneinfo import ZoneInfo

"""Config logging"""
logging.basicConfig(level=logging.INFO)

"""Config variables"""
TOKEN = getenv("BOT_TOKEN")
PROXY = getenv("PROXY")

"""Create dispatcher"""
dp = Dispatcher()

"""Command handlers"""
# Start handler
@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    try:
        await message.answer("Hi")
    except Exception as e:
        logging.error(f"Error in start handler: {e}")
        await message.answer("Sorry, couldn't process the /start")

# Date handler
@dp.message(Command("date"))
async def command_date_handler(message: Message) -> None:
    try:
        timezone_tehran = ZoneInfo("Asia/Tehran")
        now_tehran = datetime.now(timezone_tehran)
        formatted_now_tehran = now_tehran.strftime("%B %d, %Y at %I:%M %p")
        await message.reply(f"Tehran: {formatted_now_tehran}")
    except Exception as e:
        logging.error(f"Error in date handler: {e}")
        await message.reply("Sorry, couldn't process the /date.")
    
# Echo handler
@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.answer("I don't understand that message. Try /start or /date")
    except Exception as e:
        logging.error(f"Error in echo handler: {e}")
        await message.answer("Sorry, couldn't process your message.")

"""Main runner"""
async def main() -> None:
    # Set proxy
    session = AiohttpSession(proxy=PROXY) if PROXY else AiohttpSession()
    
    # Create bot
    bot = Bot(token=TOKEN, session=session)
    
    # Run bot
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Error in Main runner(#Run bot): {e}")
    finally:
        await bot.session.close()

"""Runner-file check"""
if __name__ == "__main__":
    asyncio.run(main())