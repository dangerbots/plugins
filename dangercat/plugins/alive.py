import datetime
import random
import time

from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from warbot.sql.gvar_sql import gvarstat
from . import *

#-------------------------------------------------------------------------------

ALIVE_TEMP = """
<b><i>✨ᴡᴀʀᴜsᴇʀʙᴏᴛ ɪs ᴏɴʟɪɴᴇ✨</b></i>  
<i><b> » ᴏᴡɴᴇʀ </i></b> :  <a href='tg://user?id={}'>{}</a> 
 <b>» ᴛᴇʟᴇᴛʜᴏɴ :</b> <i>{}</i>
 <b>» ᴡᴀʀᴜsᴇʀʙᴏᴛ :</b> <i>{}</i>
 <b>» sᴜᴅᴏ :</b> <i>{}</i>
 <b>» ᴜᴘᴛɪᴍᴇ :</b> <i>{}</i>
 <b>» ᴘɪɴɢ :</b> <i>{}</i>
<b><i>❤️‍🔥 <a href='https://t.me/waruserbot'>[ ᴡᴀʀᴜsᴇʀʙᴏᴛ ]</a> ❤️‍🔥</i></b>
"""

msg = """{}\n
<b><i> ❤️‍🔥 ʙᴏᴛ sᴛᴀᴛᴜs ❤️‍🔥  </b></i>
<b> ᴛᴇʟᴇᴛʜᴏɴ :</b>  <i>{}</i>
<b> ᴡᴀʀᴜsᴇʀʙᴏᴛ :</b>  <i>{}</i>
<b> ᴜᴘᴛɪᴍᴇ :</b>  <i>{}</i>
<b>ᴀʙᴜsᴇ :</b>  <i>{}</i>
<b>sᴜᴅᴏ :</b>  <i>{}</i>
"""
#-------------------------------------------------------------------------------

@hell_cmd(pattern="alive$")
async def up(event):
    cid = await client_id(event)
    Xabhish3k, HELL_USER, hell_mention = cid[0], cid[1], cid[2]
    start = datetime.datetime.now()
    hell = await eor(event, "`Building Alive....`")
    uptime = await get_time((time.time() - StartTime))
    a = gvarstat("ALIVE_PIC")
    pic_list = []
    if a:
        b = a.split(" ")
        if len(b) >= 1:
            for c in b:
                pic_list.append(c)
        PIC = random.choice(pic_list)
    else:
        PIC = "https://telegra.ph/file/9cd450f3d28848ae12026.jpg"
    end = datetime.datetime.now()
    ling = (end - start).microseconds / 1000
    omk = ALIVE_TEMP.format(Xabhish3k, HELL_USER, tel_ver, hell_ver, is_sudo, uptime, ling)
    await event.client.send_file(event.chat_id, file=PIC, caption=omk, parse_mode="HTML")
    await hell.delete()



@hell_cmd(pattern="war$")
async def hell_a(event):
    cid = await client_id(event)
    Xabhish3k, HELL_USER, hell_mention = cid[0], cid[1], cid[2]
    uptime = await get_time((time.time() - StartTime))
    am = gvarstat("ALIVE_MSG") or "<b>»» 𝘄𝗮𝗿𝘂𝘀𝗲𝗿𝗯𝗼𝘁 𝗶𝘀 𝗼𝗻𝗹𝗶𝗻𝗲 ««</b>"
    try:
        hell = await event.client.inline_query(Config.BOT_USERNAME, "alive")
        await hell[0].click(event.chat_id)
        if event.sender_id == Xabhish3k:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg.format(am, tel_ver, hell_ver, uptime, abuse_m, is_sudo), parse_mode="HTML")


CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "war", None, "Shows Inline Alive Menu with more details."
).add_warning(
  "✅ Harmless Module"
).add()
