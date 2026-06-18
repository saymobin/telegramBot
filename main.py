"""Import libraries"""
# Aiogram modules
from aiogram import Dispatcher

# Command handlers routers
from command_handlers.routers import routers_list

"""Create dispatcher"""
# Set dispatcher
dp = Dispatcher()

# Insert command-handler-routers(routers list) in dispatcher
dp.include_routers(*routers_list)