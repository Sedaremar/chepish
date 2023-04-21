from aiogram import types
import asyncio
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State
import random
import sys
import os
sys.path.append(r"E:\bot_sadar")
from starts.helps import States, dp,bot, conn,cur
from user.vostochn_horoscop import func
from user.menu.kb_menu import menu_kb
from aiogram.types import ChatActions ,InlineKeyboardMarkup, InlineKeyboardButton
from user.vostochn_horoscop import kb_vostok as kb
from user.vostochn_horoscop.kb_vostok import call_data






async def call_handlers(message:types.message):
    await message.answer("Выбери Восточный знак зодиака, для которого получить прогноз.",reply_markup=kb.horoscop_kb)
    await States.SELECT_VGOR.set()



async def vhoroscops(call:types.CallbackQuery):
    if call.data == "back":
        
        await bot.send_message(chat_id=call.from_user.id, text="Вы вернулись в меню")
        await States.MENU.set()
    else:
        url=InlineKeyboardButton("Подробнее↗",url="https://astrohelper.ru/goroskopy/na-segodnya/")

        url_in_web= InlineKeyboardMarkup(row_width=1).add(url)

        await bot.send_chat_action(call.from_user.id, ChatActions.TYPING)
        
        prediction = func.return_vostok(call.data)
        await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text=f"🀄Восточный Гороскоп:\n{prediction}",reply_markup=url_in_web)
        await States.MENU.set()



def vostok_horoscop_register(dp: Dispatcher):
    
    dp.register_message_handler(call_handlers, content_types="text",text="Восточный Гороскоп🀄", state=States.MENU)
    dp.register_callback_query_handler(vhoroscops, lambda c: c.data, text=call_data, state=States.SELECT_VGOR)

    
# 94