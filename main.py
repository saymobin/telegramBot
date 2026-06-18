"""Import libraries"""
# Other libraries
import logging

# Aiogram modules
from aiogram import Dispatcher

# Command handlers routers
from command_handlers.routers import routers_list

"""Config logging"""
logging.basicConfig(level=logging.INFO)

"""Create dispatcher"""
# Set dispatcher
dp = Dispatcher()

# Insert command-handler-routers in dispatcher
dp.include_routers(*routers_list)