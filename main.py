"""Import libraries"""
# Aiogram modules
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.client.session.aiohttp import AiohttpSession

# Other libraries
import asyncio
from os import getenv
from datetime import datetime
from zoneinfo import ZoneInfo

"""Config"""
TOKEN = getenv("BOT_TOKEN")
PROXY = getenv("PROXY")

''' Create dispatcher '''
dp = Dispatcher()

"""Command handlers"""
# Start handler
@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("Hi")

# Date handler
@dp.message(Command("date"))
async def command_date_handler(message: Message) -> None:
    timezone_tehran = ZoneInfo("Asia/Tehran")
    now_tehran = datetime.now(timezone_tehran)
    formatted_now_tehran = now_tehran.strftime("%B %d, %Y at %I:%M %p")
    await message.reply(f"Tehran: {formatted_now_tehran}")
    
# Echo handler
@dp.message()
async def echo_handler(message: Message) -> None:
    await message.answer(
        "I don't understand that message. Try /start or /date"
    )

"""Main runner"""
async def main() -> None:
    # Set proxy
    session = AiohttpSession(proxy=PROXY)
    
    # Create bot
    bot = Bot(token=TOKEN, session=session)
    
    # Run bot
    await dp.start_polling(bot)

"""Runner-file check"""
if __name__ == "__main__":
    asyncio.run(main())