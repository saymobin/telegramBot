"""Import libraries"""
# Aiogram modules
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

# Other libraries
import logging

"""Create router for start handler"""
start_router = Router()

"""Start handler"""
@start_router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    try:
        await message.answer("Hi")
    except Exception as e:
        logging.error(f"Error in start handler: {e}")
        await message.answer("Sorry, couldn't process the /start")