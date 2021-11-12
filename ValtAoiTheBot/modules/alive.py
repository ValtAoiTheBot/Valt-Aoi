# @VALTAOITHEBOT Dont remove this

from telethon import events, Button, custom
import re, os
from ValtAoiTheBot.events import register
from ValtAoiTheBot import telethn as tbot
from ValtAoiTheBot import telethn as tgbot
PHOTO = "https://telegra.ph/file/f69f2d392489d460b302e.mp4"
@register(pattern=("/alive"))
async def awake(event):
  PIKACHU = event.sender.first_name
  PIKACHU = "**◐ I Aᴍ Aᴅᴠᴀɴᴄᴇᴅ VALT AOI Rᴏʙᴏᴛ !** \n\n"
  PIKACHU += "**◐ I'ᴍ Wᴏʀᴋɪɴɢ Pʀᴏᴘᴇʀʟʏ**\n\n"
  PIKACHU += "**◐ VALT AOI! : 3.0 Lᴀᴛᴇsᴛ**\n\n"
  PIKACHU += "**◐ Mʏ Mᴀsᴛᴇʀ :** [⚡️࿐乂Ͼ🅰️🅱️🅸🅹🆃🅸🅷Ͽ乂࿐⚡️ .ᴋ](t.me/DareAbijth)\n\n"
  PIKACHU += "**◐ Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ : 1.23.0**\n\n"
  BUTTON = [[Button.url("Sᴜᴘᴘᴏʀᴛ Cʜᴀᴛ", "https://t.me/DMT_Movies_Discussion"), Button.url("UPDATES", "https://t.me/tamilblasterzzzz")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=PIKACHU,  buttons=BUTTON)
