"""Import libraries"""
# Aiogram modules
from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message

# Commands_list
from .routers import commands_list

# Other libraries
import logging

"""Create router for start handler"""
start_router = Router()

"""Start handler"""
@start_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    try:
        await message.answer(
            f"Hello {html.bold(message.from_user.full_name)}!\n"
            "this is my commands:\n"
            f"{"\n".join(commands_list)}")
    except Exception as e:
        logging.error(f"Error in start handler: {e}")
        await message.reply("Sorry, couldn't process the /start")