"""Import libraries"""

# Command handlers
from command_handlers.start_handler import start_router
from command_handlers.date_handler import date_router

# Config
from config import DATE_STATUS

# Insert command-handler-routers in dispatcher
routers_list = [start_router]
if DATE_STATUS == "1":
    routers_list.append(date_router)