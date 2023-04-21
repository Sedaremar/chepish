from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

select_citi=InlineKeyboardButton("Изменить Город",callback_data="set_citi")
back=InlineKeyboardButton("Домой🏠",callback_data="back")

select_citi_kb = InlineKeyboardMarkup(row_width=1).add(select_citi,back)
# 97