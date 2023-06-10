from telethon import TelegramClient 
import logging 
import time 

openai_key ="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"

api_id ="1125689"
api_hash ="4772d1792ed194020a8fb06a91ffb8fa"
bot_token ="6286341060:AAHQGZ2w3qDRqLBEld7aUWmtCSMMtCj1Iew"

bot =TelegramClient("mybot", api_id, api_hash).start(bot_token=bot_token) 