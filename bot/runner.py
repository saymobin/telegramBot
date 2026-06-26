"""Import libraries"""
# Other libraries
import sys
import asyncio
import logging

# Aiogram modules
from aiogram import Bot
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

# Main
from main import dp

# Config
from config import TOKEN, PROXY

"""Runner"""
async def bot_runner() -> None:
    # Set proxy
    session = AiohttpSession(proxy=PROXY) if PROXY else AiohttpSession()
    
    # Set default
    default = DefaultBotProperties(parse_mode=ParseMode.HTML)
    
    # Create bot
    bot = Bot(token=TOKEN, session=session, default=default)
    
    # Run bot
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Error in Main runner(# Run bot): {e}")
    finally:
        await bot.session.close()
        
"""Runner-file check"""
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(bot_runner())