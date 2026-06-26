"""Import libraries"""
# Aiogram modules
from aiogram import Router
from aiogram.types import Message

# Other libraries
import logging

"""Create router for echo handler"""
echo_router = Router()

"""Echo handler"""
@echo_router.message()
async def echo_handler(message: Message) -> None:
    try:
        # await message.answer("I don't understand that message. Try /start or /date or /commands_list")
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")
    except Exception as e:
        logging.error(f"Error in echo handler: {e}")
        await message.answer("Sorry, couldn't process your message.")