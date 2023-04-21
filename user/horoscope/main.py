from aiogram import types
import asyncio
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State
import random
import sys
sys.path.append(r"E:\bot_sadar")
from starts.helps import States, dp,bot, conn,cur
from user.horoscope import kb_horoscope as kb 
from user.horoscope.kb_horoscope import call_data
from aiogram.types import ChatActions,InlineKeyboardMarkup, InlineKeyboardButton

from user.horoscope import func


async def call_handler(message:types.message):
    await message.answer("Выбери знак зодиака для которого получить прогноз.",reply_markup=kb.horoscop_kb)
    await States.SELECT_GOR.set()



async def horoscops(call:types.CallbackQuery):
    if call.data == "back":
        
        await bot.send_message(chat_id=call.from_user.id, text="Вы вернулись в меню")
        await States.MENU.set()
    else:
        
        url=InlineKeyboardButton("Подробнее↗",url="https://astrohelper.ru/goroskopy/na-segodnya/")

        url_in_web= InlineKeyboardMarkup(row_width=1).add(url)
    
        
        await bot.send_chat_action(call.from_user.id, ChatActions.TYPING)
        
        prediction = func.return_horoscope(call.data)
        await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text=f"🔮Гороскоп:\n{prediction}",reply_markup=url_in_web)
        await States.MENU.set()
        
        


    
    
    








def horoscops_register_handler(dp : Dispatcher):
    dp.register_message_handler(call_handler, state=States.MENU, content_types="text", text = "Гороскоп🔮")
    dp.register_callback_query_handler(horoscops,lambda c: c.data, state=States.SELECT_GOR,text=call_data)