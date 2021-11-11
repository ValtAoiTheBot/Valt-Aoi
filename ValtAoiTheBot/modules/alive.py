# @VALTAOITHEBOT Dont remove this

from telethon import events, Button, custom
import re, os
from ValtAoiTheBot.events import register
from ValtAoiTheBot import telethn as tbot
from ValtAoiTheBot import telethn as tgbot
PHOTO = "https://telegra.ph/file/ad4d7b8a1970079468ec2.jpg"
@register(pattern=("/alive"))
async def awake(event):
  PIKACHU = event.sender.first_name
  PIKACHU = "**◐ I Aᴍ Aᴅᴠᴀɴᴄᴇᴅ VALT AOI Rᴏʙᴏᴛ !** \n\n"
  PIKACHU += "**◐ I'ᴍ Wᴏʀᴋɪɴɢ Pʀᴏᴘᴇʀʟʏ**\n\n"
  PIKACHU += "**◐ VALT AOI! : 3.0 Lᴀᴛᴇsᴛ**\n\n"
  PIKACHU += "**◐ Mʏ Mᴀsᴛᴇʀ :** [VALT AOI](t.me/ROHITH_NO_1)\n\n"
  PIKACHU += "**◐ Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ : 1.23.0**\n\n"
  BUTTON = [[Button.url("Sᴜᴘᴘᴏʀᴛ Cʜᴀᴛ", "https://t.me/pigasussupport"), Button.url("UPDATES", "https://t.me/PIGASUSUPDATES")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=PIKACHU,  buttons=BUTTON)
