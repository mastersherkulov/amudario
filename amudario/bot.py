from __future__ import unicode_literals
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Poll, PollAnswer, PollOption
from telegram.ext import InlineQueryHandler
from telegram import Bot
from amudario.settings import * 
from amudario.scraper import *
import asyncio
BOT_TOKEN = "1068899878:AAFEqEic_jx13q_IW2ixSPnLWm6W0DZkzg4"
UZBEKDEVS_BOT = Bot(token=BOT_TOKEN)


def telegram_post():
    __text = """
<b>Toshkentdagi AQSh elchixonasi havoning ifloslanishi:</b>
<i>Haqiqiy vaqtda havo sifati indeksi (AQI)</i>

AQI: <b>{}</b>
    """.format(get_aqiwgtvalue())
    __photo = open(str(BASE_DIR) + '/info.png' ,'rb')
    while True:
        try:
            send_message = asyncio.run(UZBEKDEVS_BOT.sendPhoto(chat_id=488140160, caption=__text, photo=__photo,  parse_mode="HTML", disable_notification=False))
            break
        except:
            continue