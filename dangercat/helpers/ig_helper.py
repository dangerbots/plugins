import os
import re

from TelethonHell import LOGS
from TelethonHell.clients.instaAPI import InstaGram

insta_regex = r"(?:https?:\/\/)?(?:www\.)?instagram\.com\/(?:p|tv|reel|s|stories)\/.+\/?"


async def IGDL(event, url):
    dl_path = "./insta/dl"
    if not os.path.isdir(dl_path):
        os.makedirs(dl_path)
    
    caption, file = None, None
    type = url.split("/")[3]
    IG = await InstaGram(event)
    if not IG:
        await event.edit("INSTAGRAM_SESSION not configured or Expired !")
        return file, caption
    try:
        pk = IG.media_pk_from_url(url)
        info = IG.media_info(pk).dict()
    except Exception as e:
        LOGS.info(str(e))
        return file, caption

    if type == "p":
        if info['media_type'] == 8:
            try:
                file = IG.album_download(pk, folder=dl_path)
            except Exception as e:
                LOGS.info(str(e))
                file = None

        elif info['media_type'] 
