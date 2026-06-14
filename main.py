''' Import libraries '''
# System libraries
import asyncio
from os import getenv

# Aiogram modules
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.client.session.aiohttp import AiohttpSession

''' Config '''
TOKEN = getenv("BOT_TOKEN")
PROXY = getenv("PROXY")

''' Create dispatcher '''
dp = Dispatcher()

''' Command handlers '''
# Start handler
@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("Hello! I'm a bot created with aiogram.")

''' Main runner '''
async def main() -> None:
    # Set proxy
    session = AiohttpSession(proxy=PROXY)
    
    # Create bot
    bot = Bot(token=TOKEN, session=session)
    
    # Run bot
    await dp.start_polling(bot)

''' Runner-file check '''
if __name__ == "__main__":
    asyncio.run(main())