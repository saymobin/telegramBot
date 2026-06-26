"""Import libraries"""
# Aiogram modules
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

# Other libraries
import logging

"""Create router for commands_list handler"""
commands_list_router = Router()

"""Commands_list handler"""
@commands_list_router.message(Command("commands_list"))
async def command_commands_list_handler(message: Message) -> None:
    try:
        await message.answer("/start\n/date\n/commands_list")
    except Exception as e:
        logging.error(f"Error in commands_list handler: {e}")
        await message.answer("Sorry, couldn't process the /commands_list")