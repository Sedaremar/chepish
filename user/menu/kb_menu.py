from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
#Выюор города
moscow=InlineKeyboardButton("Москва",callback_data="Moscow")
izhevsk=InlineKeyboardButton("Ижевск",callback_data="Izhevsk")

select_siti = InlineKeyboardMarkup(row_width=1).add(moscow, izhevsk)

#Меню
currencies=KeyboardButton("Курс валют💹")
currencies_cript=KeyboardButton("Курс Криптовалют💳")
weather=KeyboardButton("Погода☀")
reminder=KeyboardButton("Напоминалка⏲")
horoscop = KeyboardButton("Гороскоп🔮")
vhoroscop = KeyboardButton("Восточный Гороскоп🀄")
game = KeyboardButton("Поиграть🕹")
menu_kb = ReplyKeyboardMarkup(row_width=3,resize_keyboard=True).add(currencies,currencies_cript).add(weather,reminder,game).add(horoscop).add(vhoroscop)



ferizon=InlineKeyboardButton("Максим",url="https://kwork.ru/user/ferizon")
ezhikX=InlineKeyboardButton("Алексей",url="https://kwork.ru/user/ezhikx")
developers = InlineKeyboardMarkup(row_width=2).add(ferizon, ezhikX)


# 41

# change_file=KeyboardButton("Изменить файлы")
# changes_buttons=ReplyKeyboardMarkup(resize_keyboard=True,row_width=1).add(change_text,change_video,back)


# four_quest_3=InlineKeyboardButton("7000",callback_data="7000")
# four_ques_keyboard= InlineKeyboardMarkup(resize_keyboard=True).add(four_quest_1,four_quest_2,four_quest_3)

