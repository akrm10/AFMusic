import os
import aiohttp
import aiofiles
import yt_dlp
from yt_dlp import YoutubeDL
from pyrogram import Client, filters
from pyrogram.types import Message
from youtube_search import YoutubeSearch
from ZeMusic import app
from ZeMusic.plugins.play.filters import command
import config
from config import OWNER_ID
from ZeMusic.utils.database import is_search_enabled, enable_search, disable_search

def remove_if_exists(path):
    if os.path.exists(path):
        os.remove(path)

Nem = config.BOT_NAME + " ابحث"

@app.on_message(command(["/song", "تحميل", "بحث", Nem]))
async def song_downloader(client, message: Message):
    if not await is_search_enabled():
        return
    
    query = " ".join(message.command[1:])
    m = await message.reply_text("<b>⇜ جـارِ البحث عـن المقطـع الصـوتـي . . .</b>")
    ydl_ops = {
        'format': 'bestaudio[ext=m4a]',
        'keepvideo': True,
        'prefer_ffmpeg': False,
        'geo_bypass': True,
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': True,
    }
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"

        # تحميل الصورة المصغرة وحفظها بشكل غير متزامن
        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    async with aiofiles.open(thumb_name, mode='wb') as f:
                        await f.write(await resp.read())
        
        duration = results[0]["duration"]

    except Exception as e:
        await m.edit("- لم يتم العثـور على نتائج ؟!\n- حـاول مجـدداً . . .")
        print(str(e))
        return

    await m.edit("<b>⇜ جـارِ التحميل ▬▭ . . .</b>")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        
        rep = f"𖡃 ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ʙʏ \n@{app.username} "
        host = str(info_dict["uploader"])
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        
        await m.edit("<b>⇜ جـارِ التحميل ▬▬ . . .</b>")
        
        # التأكد من وجود الملف الصوتي قبل الإرسال
        if os.path.exists(audio_file):
            try:
                await message.reply_audio(
                    audio=audio_file,
                    caption=rep,
                    title=title,
                    performer=host,
                    thumb=thumb_name,
                    duration=dur,
                )
                await m.delete()
            except Exception as e:
                await m.edit("حدث خطأ أثناء إرسال الملف الصوتي. يرجى المحاولة مرة أخرى لاحقًا.")
                print(f"Error while sending audio file: {e}")
        else:
            await m.edit("حدث خطأ أثناء تحميل الملف الصوتي. لم يتم العثور على الملف.")
            print("Audio file not found after download.")

    except Exception as e:
        await m.edit("حدث خطأ أثناء تحميل الملف الصوتي. يرجى المحاولة مرة أخرى لاحقًا.")
        print(f"Error while downloading audio: {e}")

    try:
        remove_if_exists(audio_file)
        remove_if_exists(thumb_name)
    except Exception as e:
        print(f"Error while cleaning up files: {e}")

# أمر لتعطيل البحث
@app.on_message(command(["تعطيل البحث"]) & filters.user(OWNER_ID))
async def disable_search_command(client, message: Message):
    if not await is_search_enabled():
        await message.reply_text("<b>البحث معطل من قبل.</b>")
        return
    await disable_search()
    await message.reply_text("<b>تم تعطيل البحث بنجاح.</b>")

# أمر لتفعيل البحث
@app.on_message(command(["تفعيل البحث"]) & filters.user(OWNER_ID))
async def enable_search_command(client, message: Message):
    if await is_search_enabled():
        await message.reply_text("<b>البحث مفعل من قبل.</b>")
        return
    await enable_search()
    await message.reply_text("<b>تم تفعيل البحث بنجاح.</b>")
