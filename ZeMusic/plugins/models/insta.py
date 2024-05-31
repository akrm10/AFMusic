from pyrogram import Client, filters
import instaloader
import os
from ZeMusic import app

# تهيئة instaloader
loader = instaloader.Instaloader()

# تحميل Reels فقط
loader.context.reconsidering_profiles = False

# أمر لتحميل Reels من Instagram
@app.on_message(filters.command("انستا", prefixes="/") & filters.regex(r"https://www.instagram.com/reel/"))
def download_instagram_reel(client, message):
    try:
        # استخراج الرابط من الرسالة
        url = message.text.split(" ")[1]
        
        # محاولة تحميل الفيديو Reels باستخدام instaloader
        try:
            # تحديد Reels
            post = instaloader.Post.from_shortcode(loader.context, url.split("/")[-2])
            
            # التأكد من أن البوست يحتوي على Reels
            if not post.is_video:
                message.reply_text("الرابط لا يحتوي على فيديو Reels. يرجى إدخال رابط Reels صحيح.")
                return

            # تحميل الفيديو Reels
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
            message.reply_text(f"فشل تحميل الفيديو Reels: {e}")

    except IndexError:
        message.reply_text("الرجاء إدخال رابط Instagram Reels بعد الأمر.")

    except Exception as e:
        message.reply_text(f"حدث خطأ: {e}")

# بدء تشغيل البوت
if __name__ == "__main__":
    app.run()

