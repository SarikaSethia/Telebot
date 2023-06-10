from telethon import events 
from .. import bot 
import asyncio 
import openai 
openai_key ="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"
#openai.api_key= openai_key 

@bot.on(events.NewMessage(incoming=True,pattern= "(?i)/ask"))
async def _gpt(event):
  if event.sender_id == int(1264007252):
    await event.reply("Yess! you my Developer You Developed me very well")
  else:
    await event.reply("You are user: nice to meet you")
    