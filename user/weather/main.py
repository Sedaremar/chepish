from aiogram import types
import asyncio
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State
import random
import sys
sys.path.append(r"E:\bot_sadar")
from starts.helps import States, dp,bot, conn,cur
from user.weather import func
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatActions
from user.weather import kb_weather as kb
from user.weather.kb_weather import data


async def selected_citi(message:types.message):
    await message.answer("В каком из этих городов, показать текущую погоду?", reply_markup=kb.select_siti)
    await States.INPUT_LOC.set()



async def weather(call:types.CallbackQuery):
    if call.data == "back":
        await bot.send_message(chat_id=call.from_user.id, text = "Вы в главном меню.")
        await States.MENU.set()
    else:
        
        await bot.send_chat_action(call.from_user.id, ChatActions.TYPING)

        diction=func.return_weather(call.data)
        
        url=InlineKeyboardButton("Подробнее↗",url="https://weather.rambler.ru/")
        url_in_web= InlineKeyboardMarkup(row_width=1).add(url)


        await bot.edit_message_text(chat_id=call.from_user.id,message_id=call.message.message_id,text=f"""
{diction['spec']['loc']}:
Ночью: {diction['degree']['night']}🏙
Утром: {diction['degree']['morn']}🌅
Днем: {diction['degree']['day']}☀
Вечером: {diction['degree']['even']}🌆

{diction['spec']['wind']}💨
{diction['spec']['presur']}⏲️
{diction['spec']['sunr']}🌆

""",reply_markup=url_in_web)
        await bot.send_message(chat_id=call.from_user.id, text = "Вы в главном меню.")
        await States.MENU.set()

    









def weather_register_handler(dp : Dispatcher):
    dp.register_message_handler(selected_citi, content_types="text", text="Погода☀", state=States.MENU)
    dp.register_callback_query_handler(weather, lambda c: c.data, state=States.INPUT_LOC, text=data)
    # 203