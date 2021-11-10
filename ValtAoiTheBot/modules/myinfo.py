from telethon import custom, events, Button
import os,re
from ValtAoiTheBot import telethn as bot
from ValtAoiTheBot import telethn as tgbot
from ValtAoiTheBot.events import register 
@register(pattern="/myinfo")
async def proboyx(event):
  button = [[custom.Button.inline("CHECK",data="information")]]
  await bot.send_message(event.chat, "YOUR INFORMATION",buttons=button)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
  try:
    boy = event.sender_id
    PRO = await bot.get_entity(boy)
    SERENA = "YOUR DETAILS BY Valtaoithebot\n"
    SERENA += f"FIRST NAME : {PRO.first_name} \n"
    SERENA += f"LAST NAME : {PRO.last_name}\n"
    SERENA += f"YOU BOT : {PRO.bot} \n"
    SERENA += f"RESTRICTED : {PRO.restricted} \n"
    SERENA += f"USER ID : {boy}\n"
    SERENA += f"USERNAME : {PRO.username}\n"
    await event.answer( SERENA, alert=True)
  except Exception as e:
    await event.reply(f"{e}")
