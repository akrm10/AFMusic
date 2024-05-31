from pyrogram import Client, filters
import instaloader
import os
from ZeMusic import app

# تهيئة instaloader
loader = instaloader.Instaloader()

@app.on_message(filters.command("انستا") & filters.text)
def download_instagram_video(client, message):
    try:
        # التحقق من أن الرسالة تحتوي على رابط
        parts = message.text.split(" ")
        if len(parts) < 2:
            message.reply_text("يرجى إدخال رابط Instagram بعد الأمر.")
            return

        # استخراج الرابط من الرسالة
        url = parts[1]

        # التحقق من صحة الرابط
        if "instagram.com" not in url:
            message.reply_text("يرجى إدخال رابط Instagram صحيح.")
            return

        # محاولة تحميل الفيديو باستخدام instaloader
        try:
            # تحديد نوع الرابط (بوست، IGTV، Reel)
            shortcode = url.split("/")[-2]
            post = instaloader.Post.from_shortcode(loader.context, shortcode)
            
            # التأكد من أن البوست يحتوي على فيديو
            if not post.is_video:
                message.reply_text("الرابط لا يحتوي على فيديو. يرجى إدخال رابط يحتوي على فيديو.")
                return

            loader.download_post(post, target="downloads")

            # إرسال الفيديو للمستخدم
            for file_name in os.listdir("downloads"):
                if file_name.endswith(".mp4"):
                    video_path = os.path.join("downloads", file_name)
                    client.send_video(message.chat.id, video_path)
                    os.remove(video_path)

            # تنظيف المجلد
            os.rmdir("downloads")
        except instaloader.exceptions.InstaloaderException as e:
            message.reply_text(f"فشل تحميل الفيديو: {e}")
    except Exception as e:
        message.reply_text(f"حدث خطأ: {e}")

# بدء تشغيل البوت
if __name__ == "__main__":
    app.run()
