from aiogram import types
import asyncio
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State
import random
import sys
sys.path.append(r"E:\bot_sadar")
from starts.helps import States, dp,bot, conn,cur
from user.menu.kb_menu import menu_kb
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

back = KeyboardButton("Домой🏠")

back_kb=ReplyKeyboardMarkup(resize_keyboard=True,row_width=1).add(back)



async def back_menu(message:types.message):
    await message.answer("Вы в меню",reply_markup=menu_kb)
    await States.MENU.set()

async def free(message:types.message):
    for i in cur.execute(f"SELECT coins FROM user WHERE id = '{message.from_user.id}'"):
        coin=i[0]
    if coin < 20:
        cur.execute(f"UPDATE user SET coins = coins + 30 WHERE id = '{message.from_user.id}'")
        conn.commit()
        await message.answer("Монеты получены")
    else:
        await message.answer("Ты не можешь получить монеты, нужно иметь баланс ниже 20")

async def tap(message:types.message):
    for i in cur.execute(f"SELECT coins FROM user WHERE id = '{message.from_user.id}'"):
        bal=i[0]
    await message.answer("""
/coin {Ставка} - Шанс выйграть 50/50, при победе X2.
/slot {ставка} - Низкий шанс выйграть, при победе X4
/free - +30 Монет если баланс ниже 20
/bal - Твой баланс
""",reply_markup=back_kb)
    await States.GAMES.set()



async def coin_game(message:types.message):
    try:
        rate=int(message.get_args())
    except:
        await message.answer("Нужно передавать число.")
    else:
        for i in cur.execute(f"SELECT coins FROM user WHERE id = '{message.from_user.id}'"):
            coin=i[0]
        if rate <15:
            await message.answer("Ставки менее 15 не принимаються.")
        elif rate > 100:
            await message.answer("Савки более 100 не принимаються")
        elif coin < rate:
            await message.answer("У вас не достаточно монет на такую ставку")
        else:
            cur.execute(f"UPDATE user SET coins = coins - {rate} WHERE id = '{message.from_user.id}'")
            conn.commit()
            
            d = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
            result = random.choice(d)
            win = rate * 2
            if result == 1:
                cur.execute(f"UPDATE user SET coins = coins + {win} WHERE id = '{message.from_user.id}'")
                conn.commit()
                for i in cur.execute(f"SELECT coins FROM user WHERE id = '{message.from_user.id}'"):
                    bal=i[0]
                await message.answer(f"Ура! Ты победил. Твой выйгрыш: {win}.Твой баланс составляет: {bal}💰")
            else:
                for i in cur.execute(f"SELECT coins FROM user WHERE id = '{message.from_user.id}'"):
                    bal=i[0]
                await message.answer(f"Ты проиграл. Твой баланс составляет: {bal}")



async def slots_game(message:types.message):
    try:
        rate=int(message.get_args())
    except:
        await message.answer("Нужно передавать число.")
    else:
        for i in cur.execute(f"SELECT coins FROM user WHERE id = '{message.from_user.id}'"):
            bal=i[0]
        if rate < 30:
            await message.answer("Ставки менее 30 не принимаються.")
        elif rate > 10000:
            await message.answer("Савки более 10000 не принимаються")
        elif bal < rate:
            await message.answer("У вас не достаточно монет на такую ставку")
        else:

            cur.execute(f"UPDATE user SET coins = coins - {rate} WHERE id = '{message.from_user.id}'")
            conn.commit()

            mes=await message.answer("""
🍏 | 🍏 | 🍏""")

            subject = ["🍏","🍅","🍎","🥒","🌸","🍒","🥥","🍏","🍅","🍎","🥒","🌸","🍒","🥥","🍏","🍅","🍎","🥒","🌸","🍒","🥥","🍏","🍅","🍎","🥒","🌸","🍒","🥥","🍒","🥥","🍒","🥥"]
            for _ in range(25):
                s1=random.choice(subject)
                s2=random.choice(subject)
                s3=random.choice(subject)
                await mes.edit_text(f"{s1} | {s2} | {s3}")
            s1=random.choice(subject)
            s2=random.choice(subject)
            s3=random.choice(subject)
            await mes.edit_text(f"{s1} | {s2} | {s3}")
            await asyncio.sleep(2)
            if s1 == s2 and s1 == s3:
                win = rate * 4
                cur.execute(f"UPDATE user SET coins = coins + {win} WHERE id = '{message.from_user.id}'")
                conn.commit()
                for i in cur.execute(f"SELECT coins FROM user WHERE id = '{message.from_user.id}'"):
                    bal=i[0]
                
                await message.answer(f"Ура! Победа! Твой выйгрыш {win}! Твой баланс {bal}")
            else:
                for i in cur.execute(f"SELECT coins FROM user WHERE id = '{message.from_user.id}'"):
                    bal=i[0]
                
                await message.answer(f"Ты проиграл. Твой баланс {bal}")



async def balance(message:types.message):
    for i in cur.execute(f"SELECT coins FROM user WHERE id = '{message.from_user.id}'"):
        bal=i[0]
    await message.answer(f"Баланс {bal}")

                
            

    

# 49






        





def game_register_handler(dp : Dispatcher):

    dp.register_message_handler(tap, content_types="text", text="Поиграть🕹",state=States.MENU)
    dp.register_message_handler(back_menu, content_types="text", text="Домой🏠",state=States.GAMES)
    dp.register_message_handler(coin_game,commands = 'coin', state=States.GAMES)
    dp.register_message_handler(slots_game,commands = 'slot', state=States.GAMES)
    dp.register_message_handler(balance,commands = 'bal', state=States.GAMES)
    dp.register_message_handler(free,commands = 'free', state=States.GAMES)
    
    