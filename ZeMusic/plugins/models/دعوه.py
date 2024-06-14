from config import OWNER_ID
import asyncio
from pyrogram import Client, filters
from ZeMusic.utils.database import get_assistant
from pyrogram.types import Message
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic.core.call import Mody
from datetime import datetime, timedelta


@app.on_message(filters.video_chat_started)
async def brah(client, message):
    await msg.reply("<b>• فتحوا المكالمه اللي وده يسمعنا صوته يصعد 🦦</b>")

@app.on_message(filters.video_chat_ended)
async def brah2(client, message):
    da = message.video_chat_ended.duration
    ma = divmod(da, 60)
    ho = divmod(ma[0], 60)
    day = divmod(ho[0], 24)
    if da < 60:
       await message.reply(f"⟡ قفلنا المكالمه مدتها {da} ثواني")        
    elif 60 < da < 3600:
        if 1 <= ma[0] < 2:
            await message.reply(f"⟡ قفلنا المكالمه مدتها دقيقه")
        elif 2 <= ma[0] < 3:
            await message.reply(f"⟡ قفلنا المكالمه مدتها دقيقتين")
        elif 3 <= ma[0] < 11:
            await message.reply(f"⟡ قفلنا المكالمه مدتها {ma[0]} دقايق")  
        else:
            await message.reply(f"⟡ قفلنا المكالمه مدتها {ma[0]} دقيقه")
    elif 3600 < da < 86400:
        if 1 <= ho[0] < 2:
            await message.reply(f"⟡ قفلنا المكالمه مدتها ساعه")
        elif 2 <= ho[0] < 3:
            await message.reply(f"⟡ قفلنا المكالمه مدتها ساعتين")
        elif 3 <= ho[0] < 11:
            await message.reply(f"⟡ قفلنا المكالمه مدتها {ho[0]} ساعات")  
        else:
            await message.reply(f"⟡ قفلنا المكالمه مدتها {ho[0]} ساعة")
    else:
        if 1 <= day[0] < 2:
            await message.reply(f"⟡ قفلنا المكالمه مدتها يوم")
        elif 2 <= day[0] < 3:
            await message.reply(f"⟡ قفلنا المكالمه مدتها يومين")
        elif 3 <= day[0] < 11:
            await message.reply(f"⟡ قفلنا المكالمه مدتها {day[0]} ايام")  
        else:
            await message.reply(f"⟡ قفلنا المكالمه مدتها {day[0]} يوم")


@app.on_message(filters.video_chat_members_invited)
async def brah3(app: app, message: Message):
    text = f"↞ الحلو : {message.from_user.mention} \n↞ يبيك للمكالمه :"
    x = 0
    for user in message.video_chat_members_invited.users:
        try:
            text += f"<a href= tg://user?id={user.id} >{user.first_name}</a>"
            x += 1
        except Exception:
            pass
    try:
        await message.reply(f"{text}")
    except:
        pass
