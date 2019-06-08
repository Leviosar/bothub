__version__ = '0.1.0'

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

from telegram.ext import Updater
from commands import HANDLERS

updater = Updater(token='TOKEN', use_context=True)
dispatcher = updater.dispatcher

for handler in HANDLERS:
    dispatcher.add_handler(handler)

updater.start_polling()
updater.idle()