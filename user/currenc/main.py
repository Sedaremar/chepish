from aiogram import types
import asyncio
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State
import random
import sys
sys.path.append(r"E:\bot_sadar")
from starts.helps import States, dp,bot, conn,cur

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatActions

from user.currenc import func


async def currenc(message:types.message):

    url=InlineKeyboardButton("Подробнее↗",url="https://www.x-rates.com/")

    url_in_web= InlineKeyboardMarkup(row_width=1).add(url)
    
    await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
    currency=func.return_currenc()


    await message.answer(f"""
💹Актуальный курс валют:
1 USD = {currency["USD"]}RUB

1 EUR = {currency["EUR"]}RUB

1 KZT = {currency['KZT']}RUB

""",reply_markup=url_in_web)
# 32








def currenc_register_handler(dp : Dispatcher):
    dp.register_message_handler(currenc, content_types="text", text="Курс валют💹", state=States.MENU)