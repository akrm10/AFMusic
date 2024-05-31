from pyrogram import Client, filters
import instaloader
import os
import requests
import config
import aiohttp
import aiofiles

import yt_dlp
from yt_dlp import YoutubeDL
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message, InputTextMessageContent
from youtube_search import YoutubeSearch

from ZeMusic import app

# تهيئة instaloader
loader = instaloader.Instaloader()

@app.on_message(filters.command("انستا") & filters.text)
def download_reel(client, message):
    try:
        # استخراج الرابط من الرسالة
        url = message.text.split(" ")[1]
        
        # تحميل الفيديو باستخدام instaloader
        post = instaloader.Post.from_shortcode(loader.context, url.split("/")[-2])
        loader.download_post(post, target="downloads")
        
        # إرسال الفيديو للمستخدم
        for file_name in os.listdir("downloads"):
            if file_name.endswith(".mp4"):
                video_path = os.path.join("downloads", file_name)
                client.send_video(message.chat.id, video_path)
                os.remove(video_path)
                
        # تنظيف المجلد
        os.rmdir("downloads")
    except Exception as e:
        message.reply_text(f"حدث خطأ: {e}")

# بدء تشغيل البوت
app.run()
