import os
from pyrogram import Client, filters
from pyrogram.types import Message, User
from pyrogram import Client, emoji 
from ZeMusic import app
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ChatPermissions
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from pyrogram import filters


@app.on_message(filters.new_chat_members)
async def wel__come(client: Client, message: Message):
    chatid = message.chat.id
    await client.send_message(text=f"- انظم المطور {message.from_user.mention}\n│ \n└ʙʏ في {message.chat.title}", chat_id=chatid)



@app.on_message(filters.left_chat_member)
async def good_bye(client: Client, message: Message):
    chatid= message.chat.id
    await client.send_message(text=f"- غادر المطور\n│ \n└ʙʏ  {message.from_user.mention} ",chat_id=chatid)



"""
@app.on_chat_member_updated(filters=lambda _, response: response.new_chat_member, group=847)
async def WelcomeDev(_, response: ChatMemberUpdated):
    dev_id = 5145609515 # حط ايديك هنا
    if response.from_user.id == dev_id:
        info = await app.get_chat(dev_id)
        name = info.first_name
        bio = info.bio
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(name, user_id=dev_id)]
        ])
        await app.download_media(info.photo.big_file_id, file_name=os.path.join("downloads", "developer.jpg"))
        await app.send_photo(
            chat_id=response.chat.id,
            reply_markup=markup,
            photo="downloads/developer.jpg", 
            caption=f"↢ لقد انضم مطور السورس هنا ♥️ <a href='tg://user?id={dev_id}'>{name}</a> \n يرجي من الاعضاء احترام وجوده ☕🍀"
        )
"""
