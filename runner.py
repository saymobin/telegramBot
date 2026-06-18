"""Import libraries"""
# Other libraries
import asyncio

# Aiogram modules
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram import Bot

# Main
from main import dp

# Config
from config import TOKEN, PROXY

"""Runner"""
async def bot_runner() -> None:
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
    asyncio.run(bot_runner())