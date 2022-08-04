import asyncio
from telethon import events
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import CMD_HELP
from userbot.utils import admin_cmd


@borg.on(admin_cmd("sgban"))
async def gbun(event):
    if event.fwd_from:
        return
    gbunVar = event.text
    gbunVar = gbunVar[6:]
    mentions = "`Warning!! User 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By Admin...\n`"
    no_reason = "__Reason: not given"
    await event.edit("gbaning.....")
    asyncio.sleep(3.5)
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.sender_id))
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.sender_id
        # make meself invulnerable cuz why not xD
        if idd == 5199459106:
            await reply_message.reply("`Wait a second, This is my master!`\n**How dare you threaten to ban my master__ [\-D4RAG-/ ТЯГА](https://t.me/dragadm)......vilachil edukale veve__😏")
        else:
            jnl=("`#Gbanned `"
                  "[{}](tg://user?id={})"
                  "` was gbanned in 211groups in 92 seconds `").format(firstname, idd, firstname, idd)
            
            if len(gbunVar) > 0:
                gbunm = "`{}`".format(gbunVar)
                gbunr = "**Reason: **"+gbunm
                jnl += gbunr
            else:
                jnl += no_reason
            await reply_message.reply(jnl)
    else:
        mention = "`Warning!! User 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By Admin...\nReason: Not Given `"
        await event.reply(mention)
    await event.delete()

CMD_HELP.update(
    {
        "gbam": "**Plugin : **`gbam`\
    \n\n**Syntax : **`.gbam`\
    \n**Function : **fake gban for userbot"
    }
)
