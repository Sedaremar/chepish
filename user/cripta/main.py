from aiogram import types
import asyncio
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State
import random
import sys
sys.path.append(r"E:\bot_sadar")
from starts.helps import States, dp,bot, conn,cur
from user.cripta import func 
from aiogram.types import ChatActions,InlineKeyboardMarkup, InlineKeyboardButton




async def send_cripta(message:types.message):
    url=InlineKeyboardButton("Подробнее↗",url="https://coinmarketcap.com/ru/")

    url_in_web= InlineKeyboardMarkup(row_width=1).add(url)
    
    await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
    dict = func.return_cripta()
    await message.answer(f"""
💳Актуальный курс криптовалюты:
1 BTC = {dict['BTC']}RUB
1 ETH = {dict['ETH']}RUB
1 USDT = {dict['USDT']}RUB
1 BND = {dict['BND']}RUB
1 USDC = {dict['USDC']}RUB""",reply_markup=url_in_web)

def cripto_currency_register(dp: Dispatcher):
    dp.register_message_handler(send_cripta, content_types="text", text = "Курс Криптовалют💳", state=States.MENU)
    
# 94