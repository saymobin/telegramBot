# Import libraries
# Aiogram modules
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackData

# Other libraries
from typing import Any

# Create router for color handler
color_router = Router()

# Define a custom callback data factory
class ButtonCallback(CallbackData, prefix="btn"):
    action: str
    style: str

# Create buttons using the factory
inline_button_green = InlineKeyboardButton(
    text="سبز",
    callback_data=ButtonCallback(action="clicked!", style="success").pack(),
    style="success"
)
inline_keyboard_green = InlineKeyboardMarkup(
    inline_keyboard=[[inline_button_green]]
)

inline_button_red = InlineKeyboardButton(
    text="قرمز",
    callback_data=ButtonCallback(action="clicked!", style="danger").pack(),
    style="danger"
)
inline_keyboard_red = InlineKeyboardMarkup(
    inline_keyboard=[[inline_button_red]]
)

# Handler
@color_router.message(Command("color"))
async def start_handler(message: Message) -> Any:
    await message.reply(
        "کلیک کن، جادو ببین",
        reply_markup=inline_keyboard_green
    )
    
@color_router.callback_query(ButtonCallback.filter(F.action == "clicked!"))
async def process_callback_date(callback: CallbackQuery, callback_data: ButtonCallback) -> Any:
    current_style = callback_data.style
    
    if current_style == "success":
        await callback.message.edit_reply_markup(
            reply_markup=inline_keyboard_red
        )
    elif current_style == "danger":
        await callback.message.edit_reply_markup(
            reply_markup=inline_keyboard_green
        )
    
    await callback.answer()
    