import requests
from pyrogram import filters
from pyrogram.types import Message,InlineKeyboardButton,InlineKeyboardMarkup
from pyrogram.enums import ChatAction
from DAXXMUSIC import app
from config import BOT_USERNAME



@app.on_message(filters.command("cosplay"))
async def cosplay(_,msg):
    img = requests.get("https://sugoi-api.vercel.app/cosplay").json()
    await msg.reply_photo(img, caption=f"ABSOLUTE CINEMA")