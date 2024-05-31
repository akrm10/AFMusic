from pyrogram import Client, filters
import instaloader
import os

# إعدادات البوت
api_id =  API_ID   # استبدلها بـ API ID الخاص بك
api_hash =  API_HASH   # استبدلها بـ API Hash الخاص بك
bot_token =  BOT_TOKEN   # استبدلها بـ Bot Token الخاص بك

# تهيئة العميل
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

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
