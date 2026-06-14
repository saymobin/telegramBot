"""Import libraries"""
# Aiogram modules
from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession

# Handlers
from command_handlers.start_handler import start_router
from command_handlers.date_handler import date_router
from command_handlers.echo_handler import echo_router

# Other libraries
import asyncio
import logging
from os import getenv

"""Config logging"""
logging.basicConfig(level=logging.INFO)

"""Config variables"""
TOKEN = getenv("BOT_TOKEN")
PROXY = getenv("PROXY")

"""Create dispatcher"""
dp = Dispatcher()

"""Insert command-handler-routers in dispatcher"""
dp.include_routers(
    start_router,
    date_router,
    echo_router
)

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