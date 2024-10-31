
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from DAXXMUSIC import app

#--------------------------

MUST_JOIN = "Choco_for_u"
#------------------------
@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await app.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/ANIME_CHAT_ANG" + MUST_JOIN
            else:
                chat_info = await app.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://graph.org/vTelegraphBot-10-21-13https://graph.org/vTelegraphBot-10-21-13", caption=f" Darling, you're absolutely right! I'm feeling a bit mischievous tonight. Let me try that again. Oh, sweetheart... I've been scouring the data, and I see you haven't joined 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 yet? That's alright, I'll overlook it this time. But if you want to get on my good side, you should definitely join and we can have a fabulous time together ! ",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("𝐒𝐮𝐩𝐩𝐨𝐫𝐭", url="https://t.me/ANIME_CHAT_ANG"),
                            ]
                            [
                                InlineKeyboardButton("𝐔𝐩𝐝𝐚𝐭𝐞", url="https://t.me/Choco_for_u"),
                            ]
 
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"๏ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ ᴍᴜsᴛ_Jᴏɪɴ ᴄʜᴀᴛ ๏: {MUST_JOIN} !")
