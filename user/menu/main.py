from aiogram import types
import asyncio
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State
import random
import sys
sys.path.append(r"E:\bot_sadar")
from starts.helps import States, dp,bot, conn,cur
from user.menu import kb_menu as kb


# <a href=""> TEXT </a>
async def by(message:types.message):
    await message.answer("""
Разработчик этого бота:
🖥<a href="https://vk.com/tzredam">Андрей</a>(Sedaremar) - Главный разработчик.

Профиль в ВК👇
""",reply_markup=kb.developers)


async def start_bot(message:types.message):
    
    if cur.execute(f"SELECT id FROM user WHERE id = '{message.from_user.id}'").fetchone() is None:
        cur.execute("INSERT INTO user VALUES (?,?,?)",(message.from_user.id, 500,"None"))
        conn.commit()
        
    
    await message.answer("Добро пожаловать!", reply_markup=kb.menu_kb)
    
    await States.MENU.set()

# 49






        





def user_register_handler(dp : Dispatcher):
    dp.register_message_handler(start_bot,commands = 'start')
    dp.register_message_handler(by,commands = 'by', state="*")
    
    