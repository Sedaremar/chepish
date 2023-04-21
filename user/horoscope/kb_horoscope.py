from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

oven=InlineKeyboardButton("♈Овен",callback_data="aries")
telec=InlineKeyboardButton("♉Телец",callback_data="taurus")
blizneci=InlineKeyboardButton("♊Близнецы",callback_data="gemini")
rak=InlineKeyboardButton("♋Рак",callback_data="cancer")
lev=InlineKeyboardButton("♌Лев",callback_data="leo")
deva=InlineKeyboardButton("♍Дева",callback_data="virgo")
vesi=InlineKeyboardButton("♎Весы",callback_data="libra")
skorpion=InlineKeyboardButton("♏Скорпион",callback_data="scorpio")
sagittarius=InlineKeyboardButton("♐Стрелец",callback_data="sagittarius")
kozerok=InlineKeyboardButton("♑Козерог",callback_data="capricorn")
vodolei=InlineKeyboardButton("♒Водолей",callback_data="aquarius")
ribi=InlineKeyboardButton("♓Рыбы",callback_data="pisces")
back=InlineKeyboardButton("Домой🏠",callback_data="back")

horoscop_kb = InlineKeyboardMarkup(row_width=2).add(oven,telec,blizneci,rak,lev,deva,vesi,skorpion,sagittarius,kozerok,vodolei,ribi).add(back)

call_data=["aries","taurus","gemini","cancer","leo","virgo","libra","scorpio","sagittarius","capricorn","aquarius","pisces","back"]
