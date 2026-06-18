"""Import libraries"""

# Command handlers
from .start_handler import start_router
from .date_handler import date_router
from .commands_list_handler import commands_list_router

# Config
from config import DATE_STATUS

# Insert command-handler-routers in dispatcher
routers_list = [start_router, commands_list_router]
if DATE_STATUS == "1":
    routers_list.append(date_router)