from pyrogram import Client
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from ZeMusic import app
import os


@app.on_chat_member_updated(filters=lambda _, response: response.new_chat_member, group=847)
async def WelcomeDev(_, response: ChatMemberUpdated):
    dev_id = 6600943153 # حط ايديك هنا
    if response.from_user.id == dev_id:
        info = await app.get_chat(dev_id)
        name = info.first_name
        
        await app.send_message(
            chat_id=response.chat.id,
            caption=f"⟡ وسع وسع المطور {name} دخل الجروب.\n⟡ {bio}")
    
