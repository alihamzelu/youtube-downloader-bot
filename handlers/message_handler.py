import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.state import user_state, user_data
from utils.downloader import download_audio

def register_message_handler(bot):

    @bot.message_handler(func=lambda message: True)
    def handle_message(message):

        user_id = message.from_user.id
        state = user_state.get(user_id)

        # 🎬 VIDEO FLOW
        if state == "waiting_link_video":

            user_data[user_id] = message.text

            markup = InlineKeyboardMarkup()
            markup.add(
                InlineKeyboardButton("🎬 360p", callback_data="360"),
                InlineKeyboardButton("🎬 720p", callback_data="720"),
                InlineKeyboardButton("🎬 1080p", callback_data="1080")
            )

            bot.send_message(
                message.chat.id,
                "🎬 Choose video quality:",
                reply_markup=markup
            )

            user_state[user_id] = "choosing_quality"

        # 🎵 AUDIO FLOW
        elif state == "waiting_link_audio":

            status_msg = bot.send_message(
                message.chat.id,
                "🎵 Processing audio..."
            )

            try:
                file_path = download_audio(message.text)

                bot.edit_message_text(
                    "📤 Uploading audio...",
                    message.chat.id,
                    status_msg.message_id
                )

                # --- ⚡ اضافه شدن تایم‌اوت ۵ دقیقه‌ای برای آپلود موزیک‌های سنگین یوتیوب ⚡ ---
                with open(file_path, "rb") as audio:
                    bot.send_audio(
                        message.chat.id,
                        audio,
                        caption="🎵 Your audio is ready!",
                        timeout=300  
                    )

                # 🧼 حذف پیام موقت وضعیت (Uploading...) بعد از ارسال موفق صدا
                try:
                    bot.delete_message(message.chat.id, status_msg.message_id)
                except Exception:
                    pass

                os.remove(file_path)

            except Exception as e:
                print(f"Error in audio upload: {e}") # لاگ انداختن خطای واقعی در ترمینال
                
                # 🧼 حذف پیام موقت وضعیت در صورت بروز خطا
                try:
                    bot.delete_message(message.chat.id, status_msg.message_id)
                except Exception:
                    pass

                bot.send_message(
                    message.chat.id,
                    "❌ Failed to download audio. Try again."
                )

            user_state[user_id] = "done"