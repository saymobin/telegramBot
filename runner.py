"""Import libraries"""
# Other libraries
from dotenv import load_dotenv
load_dotenv()

import asyncio
import logging
from os import getenv

# Aiogram modules
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram import Bot

# Main
from main import dp

"""Config logging"""
logging.basicConfig(level=logging.INFO)

"""Config variables"""
TOKEN = getenv("BOT_TOKEN1")
PROXY = getenv("PROXY")

"""Runner"""
async def bot_runner(dp) -> None:
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
    asyncio.run(bot_runner(dp=dp))