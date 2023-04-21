from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

krisa=InlineKeyboardButton("Крыса",callback_data="rat")
byk=InlineKeyboardButton("Бык",callback_data="ox")
tiger=InlineKeyboardButton("Тигр",callback_data="tiger")
krol=InlineKeyboardButton("Кролик",callback_data="rabbit")
drakon=InlineKeyboardButton("Дракон",callback_data="dragon")
zmea=InlineKeyboardButton("Змея",callback_data="snake")
loshad=InlineKeyboardButton("Лошадь",callback_data="horse")
koza=InlineKeyboardButton("Коза",callback_data="sheep")
obezana=InlineKeyboardButton("Обезьяна",callback_data="monkey")
petuh=InlineKeyboardButton("Петух",callback_data="rooster")
dog=InlineKeyboardButton("Собака",callback_data="dog")
pig=InlineKeyboardButton("Свинья",callback_data="pig")
back=InlineKeyboardButton("Домой🏠",callback_data="back")

horoscop_kb = InlineKeyboardMarkup(row_width=2).add(krisa,byk,tiger,krol,drakon,zmea,loshad,koza,obezana,petuh,dog,pig).add(back)

call_data=["rat","ox","tiger","rabbit","dragon","snake","horse","sheep","monkey","rooster","dog","pig","back"]