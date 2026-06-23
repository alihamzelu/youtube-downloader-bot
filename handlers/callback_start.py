from utils.state import user_state

def register_callback_start(bot):

    @bot.callback_query_handler(func=lambda call: call.data in ["video", "audio", "helpbtn"])
    def handle(call):

        user_id = call.from_user.id

        if call.data == "video":

            user_state[user_id] = "waiting_link_video"

            bot.edit_message_text(
                "🎬 Send me a YouTube link to download video:",
                call.message.chat.id,
                call.message.message_id
            )

        elif call.data == "audio":

            user_state[user_id] = "waiting_link_audio"

            bot.edit_message_text(
                "🎵 Send me a YouTube link to extract audio:",
                call.message.chat.id,
                call.message.message_id
            )

        elif call.data == "helpbtn":

            bot.edit_message_text(
                """📥 YouTube Downloader Help

1️⃣ Send a YouTube link
2️⃣ Choose video or audio
3️⃣ Wait for processing
4️⃣ Get your file

⚡ Simple & fast""",
                call.message.chat.id,
                call.message.message_id
            )