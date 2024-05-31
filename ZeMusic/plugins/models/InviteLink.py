from ZeMusic import app
from pyrogram import Client, filters
from pyrogram.errors import ChatIdInvalid
from pyrogram.errors import ChatAdminRequired, ChatNotModified, ChatIdInvalid, FloodWait, InviteHashExpired, UserNotParticipant
import os
import json
from pyrogram.types import Message
from ZeMusic.misc import SUDOERS


@app.on_message(filters.command(["رابط"]) & SUDOERS)
async def link_command_handler(client: Client, message: Message):
    if len(message.command) != 2:
        await message.reply("الاستخدام غير صحيح. يرجى استخدام الصيغة :\n\n/رابط [ايدي الجروب]")
        return

    group_id = message.command[1]
    file_name = f"group_{group_id}.txt"

    try:
        chat = await client.get_chat(int(group_id))

        if chat is None:
            await message.reply("غير قادر على الحصول على معلومات المجموعه المحدده.")
            return

        try:
            invite_link = await client.export_chat_invite_link(chat.id)
        except FloodWait as e:
            await message.reply(f"FloodWait: {e.x} seconds. Retrying in {e.x} seconds.")
            return

        group_data = {
            "الايدي": chat.id,
            "النوع": str(chat.type),
            "الاسم": chat.title,
            "عدد_الاعضاء": chat.members_count,
            "الوصف": chat.description,
            "معرف_مركز_البيانات": chat.dc_id,
            "تقييد_حفظ_المحتوى": chat.has_protected_content,
            "الرابط": invite_link,
        }

        with open(file_name, "w", encoding="utf-8") as file:
            for key, value in group_data.items():
                file.write(f"{key}: {value}\n")

        await client.send_document(
            chat_id=message.chat.id,
            document=file_name,
            caption=f"معلومات مجموعه :\n{chat.title}\n𝘉𝘺 : @{app.username}"
        )

    except Exception as e:
        await message.reply(f"البوت ليس مشرف في المجموعه او ليس لديه صلاحيه دعوة المستخدمين.\n\nرساله الخطاء: {str(e)}")

    finally:
        if os.path.exists(file_name):
            os.remove(file_name)
