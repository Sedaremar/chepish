from aiogram import types
import asyncio
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State
import random
import sys
sys.path.append(r"E:\bot_sadar")
from starts.helps import States, dp,bot, conn,cur
from user.settings import kb_settings as kb
from user.menu import kb_menu as kb1


async def setting(message:types.message):
    await message.answer("⚙", reply_markup=types.ReplyKeyboardRemove())
    await message.answer("Меню настроек⚙",reply_markup=kb.select_citi_kb)
    await States.SETTINGS.set()


async def tap(call:types.CallbackQuery):
    if call.data == "set_citi":
        await bot.edit_message_text(chat_id=call.from_user.id,message_id=call.message.message_id,text="Выбери свой город из представленных:", reply_markup=kb1.select_siti)
        await States.INPUT_LOC.set()
    elif call.data == "back":
        await bot.send_message(chat_id=call.from_user.id, text = "Вы в меню",reply_markup=kb1.menu_kb)
        await States.MENU.set()


    
    





        





def set_register_handler(dp : Dispatcher):
    dp.register_message_handler(setting, content_types="text", text="Настройки⚙", state=States.MENU)
    dp.register_callback_query_handler(tap, lambda c: c.data, text=["set_citi","back"],state=States.SETTINGS)
    # 111