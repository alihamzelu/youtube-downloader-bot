from keyboards.main_kb import start_keyboard

def register_start_handler(bot):

    @bot.message_handler(commands=['start'])
    def start(message):

        bot.send_message(
            message.chat.id,
            f"""👋 Welcome {message.from_user.first_name}

🎬 YouTube Downloader Bot

✨ Download videos or audio in seconds
⚡ Fast • Simple • Free

👇 Choose an option:""",
            reply_markup=start_keyboard()
        )