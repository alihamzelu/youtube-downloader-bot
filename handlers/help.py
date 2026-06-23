def register_help_handler(bot):

    @bot.message_handler(commands=['help'])
    def help_cmd(message):

        bot.send_message(
            message.chat.id,
            "📥 Send a YouTube link and choose format"
        )