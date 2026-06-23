from .start import register_start_handler
from .help import register_help_handler

def register_all_handlers(bot):
    register_start_handler(bot)
    register_help_handler(bot)