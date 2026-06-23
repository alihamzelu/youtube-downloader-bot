import telebot
from config import API_TOKEN

from handlers import register_all_handlers
from handlers.callback_start import register_callback_start
from handlers.callback_quality import register_callback_quality
from handlers.message_handler import register_message_handler

bot = telebot.TeleBot(API_TOKEN)

register_all_handlers(bot)

register_callback_start(bot)
register_callback_quality(bot)

register_message_handler(bot)

bot.polling()