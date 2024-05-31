from ZeMusic import app
import os
import yt_dlp
from pyrogram import Client, filters
from pyrogram.types import Message


@app.on_message(filters.command(["انستا"], ["/", "!", "."]))
async def download_instareels(client: Client, message: Message):
    try:
        reel_ = message.command[1]
    except IndexError:
        await message.reply_text("أعطني رابطا لتحميل المقطع...")
        return

    if not reel_.startswith("https://www.instagram.com/reel/"):
        await message.reply_text("من أجل الحصول على النتائج الصحيحة، من الضروري وجود رابط صالح. يرجى تزويدي بالرابط المطلوب.")
        return

    ydl_opts = {
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
        'ignoreerrors': True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(reel_, download=True)
            
            if info_dict is None:
                await message.reply_text("لم أتمكن من استخراج معلومات الفيديو. ربما يكون الرابط غير صالح.")
                return

            video_file = ydl.prepare_filename(info_dict)
            if not os.path.exists(video_file):
                await message.reply_text("حدث خطأ أثناء تنزيل الفيديو. الملف غير موجود.")
                return

        await message.reply_video(video_file)
        
        # تنظيف الملف بعد الإرسال
        if os.path.exists(video_file):
            os.remove(video_file)
    except Exception as e:
        await message.reply_text(f"حدث خطأ أثناء تحميل الفيديو: {e}")
