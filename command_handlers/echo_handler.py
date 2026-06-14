"""Import libraries"""
# Aiogram modules
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

# Other libraries
import logging

"""Create router for echo handler"""
echo_router = Router()

"""echo handler"""
@echo_router.message(Command("echo"))
async def command_echo_handler(message: Message) -> None:
    try:
        await message.answer("I don't understand that message. Try /start or /date")
    except Exception as e:
        logging.error(f"Error in echo handler: {e}")
        await message.answer("Sorry, couldn't process your message.")