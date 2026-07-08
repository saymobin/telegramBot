"""Import libraries"""
# Command handlers
from .date_handler import date_router as date
from .echo_handler import echo_router as echo
from .color_handler import color_router as color

# Config
from config import DATE_STATUS, ECHO_STATUS, COLOR_STATUS

# Create routers list
routers_list = []
commands_list = ["/start", "/commands_list"]
if DATE_STATUS == "on":
    routers_list.append(date)
    commands_list.append("/date")
if COLOR_STATUS == "on":
    routers_list.append(color)
    commands_list.append("/color")
if ECHO_STATUS == "on":
    routers_list.append(echo)
    commands_list.append("/echo")