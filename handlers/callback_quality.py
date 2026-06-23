import os
from utils.state import user_state, user_data
from utils.downloader import download_video

def register_callback_quality(bot):

    @bot.callback_query_handler(func=lambda call: call.data in ["360", "720", "1080"])
    def handle_quality(call):

        user_id = call.from_user.id
        quality = int(call.data)  # ✅ تبدیل به integer
        link = user_data.get(user_id)

        if not link:
            bot.send_message(
                call.message.chat.id,
                "❌ Session expired. Please start again with /start"
            )
            return

        # 🧼 حذف پیام قبلی (که حاوی دکمه‌های انتخاب کیفیت بود)
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception:
            pass

        status_msg = bot.send_message(
            call.message.chat.id,
            f"🎬 Downloading {quality}p..."
        )

        try:
            file_path = download_video(link, quality)  # ✅ integer بفرست

            bot.edit_message_text(
                "📤 Uploading video...",
                call.message.chat.id,
                status_msg.message_id
            )

            # --- ⚡ اضافه شدن تایم‌اوت ۵ دقیقه‌ای برای جلوگیری از ارور رایت ⚡ ---
            with open(file_path, "rb") as video:
                bot.send_video(
                    call.message.chat.id,
                    video,
                    caption=f"✅ Done! ({quality}p)",
                    timeout=300  # ۵ دقیقه زمان به پایتون میده تا ویدیو رو آپلود کنه
                )

            # 🧼 حذف پیام موقت وضعیت (Uploading...) بعد از ارسال موفق ویدیو
            try:
                bot.delete_message(call.message.chat.id, status_msg.message_id)
            except Exception:
                pass

            os.remove(file_path)

        except Exception as e:
            print(f"💥 Upload/Download Error Detail: {e}")  # نمایش ارور واقعی و کامل در ترمینال شما
            
            # 🧼 حذف پیام موقت وضعیت در صورت بروز خطا
            try:
                bot.delete_message(call.message.chat.id, status_msg.message_id)
            except Exception:
                pass

            bot.send_message(
                call.message.chat.id,
                f"❌ Download failed: {str(e)[:80]}"
            )

        user_state[user_id] = "done"