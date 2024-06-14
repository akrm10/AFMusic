from pyrogram import Client, filters
from pyrogram.types import ChatMemberUpdated
from ZeMusic import app
import os

@app.on_chat_member_updated(group=847)
async def WelcomeDev(_, response: ChatMemberUpdated):
    dev_id = 5145609515 # حط ايديك هنا
    # التحقق من أن العضو الجديد هو المطور وحالته الجديدة هي "member"
    if response.new_chat_member.user.id == dev_id and response.new_chat_member.status == "member":
        info = await app.get_chat(dev_id)
        name = info.first_name
        await app.send_message(
            chat_id=response.chat.id,
            text=f"↢ لقد انضم مطور السورس هنا ♥️ <a href='tg://user?id={dev_id}'>{name}</a> \n يرجي من الاعضاء احترام وجوده ☕🍀",
            parse_mode="html"
        )
