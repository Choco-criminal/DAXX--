# SOURCE https://github.com/Team-ProjectCodeX
# CREATED BY https://t.me/O_okarma
# PROVIDED BY https://t.me/ProjectCodeX
# NEKOS

# <============================================== IMPORTS =========================================================>
import nekos
from telethon import events

from Database.mongodb.toggle_mongo import is_nekomode_on, nekomode_off, nekomode_on
from Mikobot import tbot
from Mikobot.state import state  # Import the state function

# <=======================================================================================================>

url_sfw = "https://nekos.best/api/v2/"

allowed_commands = [
    "waifu",
    "neko",
    "shinobu",
    "megumin",
    "bully",
    "cuddle",
    "cry",
    "hug",
    "awoo",
    "kiss",
    "lick",
    "pat",
    "smug",
    "bonk",
    "yeet",
    "blush",
    "smile",
    "spank",
    "wave",
    "highfive",
    "handhold",
    "nom",
    "bite",
    "glomp",
    "slap",
    "hTojiy",
    "wink",
    "poke",
    "dance",
    "cringe",
    "tickle",
]


# <================================================ FUNCTION =======================================================>

@tbot.on(events.NewMessage(pattern=r"/(?:{})".format("|".join(allowed_commands))))
async def nekomode_commands(event):
    chat_id = event.chat_id
    nekomode_status = await is_nekomode_on(chat_id)
    if nekomode_status:
        target = event.raw_text[1:].lower()  # Remove the slash before the command
        if target in allowed_commands:
            url = f"{url_sfw}{target}"

            response = await state.get(url)
            result = response.json()
            animation_url = result["url"]

            # Send animation
            await event.respond(file=animation_url)


