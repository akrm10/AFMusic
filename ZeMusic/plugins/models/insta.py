from ZeMusic import app
from pyrogram import Client, filters
from pyrogram.types import Message
import yt_dlp

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
            video_file = ydl.prepare_filename(info_dict)

        await message.reply_video(video_file)
        
        # تنظيف الملف بعد الإرسال
        if os.path.exists(video_file):
            os.remove(video_file)
    except Exception as e:
        await message.reply_text(f"حدث خطأ أثناء تحميل الفيديو: {e}")




"""
@app.on_message(filters.command(["تحميل استوري"], ["/", "!", "."]))
async def instagram_reel(client, message):
    if len(message.command) == 2:
        url = message.command[1]
        response = requests.post(f"https://lexica-api.vercel.app/download/instagram?url={url}")
        data = response.json()

        if data['code'] == 2:
            media_urls = data['content']['mediaUrls']
            if media_urls:
                video_url = media_urls[0]['url']
                await message.reply_video(f"{video_url}")
            else:
                await message.reply("لم يتم العثور على فيديو في الرد. قد يكون الحساب خاصا.")
        else:
            await message.reply("لم يكن الطلب ناجحا.")
    else:
        await message.reply("يرجى تقديم عنوان URL صالح لـ Instagram باستخدام الأمر تحميل استوري..")
"""
