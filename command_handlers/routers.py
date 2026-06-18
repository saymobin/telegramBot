"""Import libraries"""
# Command handlers
from .start_handler import start_router
from .commands_list_handler import commands_list_router
from .date_handler import date_router
from .echo_handler import echo_router

# Config
from config import DATE_STATUS, ECHO_STATUS

# Create routers list
routers_list = [start_router, commands_list_router]
if DATE_STATUS == "1":
    routers_list.append(date_router)
if ECHO_STATUS == "1":
    routers_list.append(echo_router)