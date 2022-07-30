import datetime
import time

from warbot import *
from warbot.clients import *
from warbot.config import Config
from warbot.helpers import *
from warbot.utils import *
from warbot.random_strings import *
from warbot.version import __hell__
from warbot.sql.gvar_sql import gvarstat
from telethon import version

hell_logo = "./warbot/resources/pics/hellbot_logo.jpg"
cjb = "./warbot/resources/pics/cjb.jpg"
restlo = "./warbot/resources/pics/rest.jpeg"
shuru = "./warbot/resources/pics/shuru.jpg"
shhh = "./warbot/resources/pics/chup_madarchod.jpeg"
hl = Config.HANDLER
shl = Config.SUDO_HANDLER
hell_ver = __hell__
tel_ver = version.__version__

async def get_user_id(ids):
    if str(ids).isdigit():
        userid = int(ids)
    else:
        userid = (await bot.get_entity(ids)).id
    return userid

is_sudo = "True" if gvarstat("SUDO_USERS") else "False"

abus = Config.ABUSE
if abus == "ON":
    abuse_m = "Enabled"
else:
    abuse_m ="Disabled"


my_channel = Config.MY_CHANNEL or "waruserbot"
my_group = Config.MY_GROUP or "waruserbotsupport"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")

chnl_link = "https://t.me/waruserbot"
hell_channel = f"[WarUserBot]({chnl_link})"
grp_link = "https://t.me/waruserbotsupport"
hell_grp = f"[Waruserbot Group]({grp_link})"

WELCOME_FORMAT = """**Use these fomats in your welcome note to make them attractive.**
  {mention} :  To mention the user
  {title} : To get chat name in message
  {count} : To get group members
  {first} : To use user first name
  {last} : To use user last name
  {fullname} : To use user full name
  {userid} : To use userid
  {username} : To use user username
  {my_first} : To use my first name
  {my_fullname} : To use my full name
  {my_last} : To use my last name
  {my_mention} : To mention myself
  {my_username} : To use my username
"""
# will add more soon


