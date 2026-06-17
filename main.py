"""Import libraries"""
# Other libraries
import logging

# Aiogram modules
from aiogram import Dispatcher

# Command handlers
from command_handlers.start_handler import start_router
from command_handlers.date_handler import date_router, DATE_STAT

"""Config logging"""
logging.basicConfig(level=logging.INFO)

"""Create dispatcher"""
# Set dispatcher
dp = Dispatcher()

# Insert command-handler-routers in dispatcher
routers_list = [start_router]
if int(DATE_STAT) == 1:
    routers_list.append(date_router)
dp.include_routers(*routers_list)