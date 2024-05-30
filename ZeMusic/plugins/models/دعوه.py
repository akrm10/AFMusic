from config import OWNER_ID
import asyncio
from pyrogram import Client, filters
from ZeMusic.utils.database import get_assistant
from pyrogram.types import Message
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic.core.call import Mody
from datetime import datetime, timedelta

call_start_time = {}

@app.on_message(filters.video_chat_started)
async def brah(_, msg):
    chat_id = msg.chat.id
    call_start_time[chat_id] = datetime.now()
    await msg.reply("<b>• فتحوا المكالمه اللي وده يسمعنا صوته يصعد 🦦</b>")

@app.on_message(filters.video_chat_ended)
async def brah2(_, msg):
    chat_id = msg.chat.id
    start_time = call_start_time.pop(chat_id, None)
    if start_time:
        duration = datetime.now() - start_time
        days, seconds = duration.days, duration.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60

        if days > 0:
            duration_str = f"{days} أيام و {hours} ساعات"
        elif hours > 0:
            duration_str = f"{hours} ساعات و {minutes} دقائق"
        else:
            duration_str = f"{minutes} دقائق و {seconds} ثواني"

        await msg.reply(f"<b>• قفلنا المكالمه مدة المكالمه {duration_str}</b>")
    else:
        await msg.reply("<b>• قفلنا المكالمه</b>")

@app.on_message(filters.video_chat_members_invited)
async def brah3(app: app, message: Message):
    text = f"↞ الحلو : {message.from_user.mention} \n↞ يبيك للمكالمه :"
    x = 0
    for user in message.video_chat_members_invited.users:
        try:
            text += f"<a href='tg://user?id={user.id}'>{user.first_name}</a>"
            x += 1
        except Exception:
            pass
    try:
        await message.reply(f"{text}")
    except:
        pass
