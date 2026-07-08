"""Import libraries"""
# Aiogram modules
from aiogram import Dispatcher

# Command handlers routers
from command_handlers.routers import routers_list
from command_handlers.start_handler import start_router as start
from command_handlers.commands_list_handler import commands_list_router as commands_list

"""Create dispatcher"""
# Set dispatcher
dp = Dispatcher()

# Insert command-handler-routers(routers list) in dispatcher
routers_list[:0] = [start, commands_list]
dp.include_routers(*routers_list)