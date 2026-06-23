from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def start_keyboard():

    markup = InlineKeyboardMarkup(row_width=1)

    markup.add(
        InlineKeyboardButton("🎥 Download Video", callback_data="video"),
        InlineKeyboardButton("🎵 Extract Audio", callback_data="audio"),
        InlineKeyboardButton("❓ Help", callback_data="helpbtn")
    )

    return markup