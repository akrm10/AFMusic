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

def remove_if_exists(path):
    if os.path.exists(path):
        os.remove(path)

Nem = config.BOT_NAME + " ابحث"

@app.on_message(command(["/song", "تحميل", "بحث", Nem]))
async def song_downloader(client, message: Message):
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
                    f = await aiofiles.open(thumb_name, mode='wb')
                    await f.write(await resp.read())
                    await f.close()
        
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
        
        # فتح الملف الصوتي وإرساله بشكل غير متزامن
        try:
            async with aiofiles.open(audio_file, mode='rb') as af:
                await message.reply_audio(
                    audio=af,
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

    except Exception as e:
        await m.edit("حدث خطأ أثناء تحميل الملف الصوتي. يرجى المحاولة مرة أخرى لاحقًا.")
        print(f"Error while downloading audio: {e}")

    try:
        remove_if_exists(audio_file)
        remove_if_exists(thumb_name)
    except Exception as e:
        print(f"Error while cleaning up files: {e}")
