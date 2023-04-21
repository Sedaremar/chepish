from aiogram import types
import asyncio
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State
import random
import sys
sys.path.append(r"E:\bot_sadar")
from starts.helps import States, dp,bot, conn,cur
from user.reminder import kb_reminded as kb
from user.menu.kb_menu import menu_kb
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


async def reminder_handler(message:types.message):
    await message.answer("""В следующем сообщении вам необходимо отправить текст напоминалки. Он придет вам через установленое вами время.
Пример: Выключить плиту, Покормить собаку, Позвонить другу...""",reply_markup=kb.back_kb)
    await States.TEXT_REMINDED.set()

async def text_reminded(message:types.message):
    if message.text == "Домой🏠":
        await message.answer("Вы в меню",reply_markup=menu_kb)
        await States.MENU.set()
    else:
        
        cur.execute(f"UPDATE user SET remind = '{message.text}' WHERE id = '{message.from_user.id}'")
        conn.commit()
        await message.answer("В следующем сообщении отправь то количество минут, через которое должно сработать напоминание.",reply_markup=kb.back_kb1)
        await States.TIME_REMINDED.set()

async def time_reminded(message:types.message):
    if message.text == "Домой🏠":
        await message.answer("Вы в меню",reply_markup=menu_kb)
        await States.MENU.set()
    elif message.text == "Случайное Время⏳":
        random_time = random.randrange(1,300) 
        await message.answer(f"Таймер поставлен на {random_time}Мин",reply_markup=menu_kb)
        await States.MENU.set()


        for i in cur.execute(f"SELECT remind FROM user WHERE id = '{message.from_user.id}'"):
            text=i[0]
        await asyncio.sleep(random_time*60)

        await message.answer(f"Напоминалка:\n{text}")

        
    else:
        try:
            d=float(message.text)
        except:
            await message.answer("Не правильно набрано время!")
        else:
            await message.answer(f"Таймер поставлен на {message.text}Мин",reply_markup=menu_kb)
            await States.MENU.set()

            for i in cur.execute(f"SELECT remind FROM user WHERE id = '{message.from_user.id}'"):
                text=i[0]
            await asyncio.sleep(float(message.text)*60)

            await message.answer(f"⏰Напоминалка:\n{text}")


def reminder_timer_register(dp: Dispatcher):
    dp.register_message_handler(reminder_handler, content_types="text", text = "Напоминалка⏲", state=States.MENU)
    dp.register_message_handler(text_reminded, content_types="text", state=States.TEXT_REMINDED)
    dp.register_message_handler(time_reminded, content_types="text", state=States.TIME_REMINDED)
# 94