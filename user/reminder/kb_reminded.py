from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

back = KeyboardButton("Домой🏠")
random_time=KeyboardButton("Случайное Время⏳")
back_kb=ReplyKeyboardMarkup(resize_keyboard=True,row_width=1).add(back)
back_kb1=ReplyKeyboardMarkup(resize_keyboard=True,row_width=1).add(back,random_time)
# 52