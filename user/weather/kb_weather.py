from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
moscow=InlineKeyboardButton("Москва",callback_data="v-moskve")
izhevsk=InlineKeyboardButton("Ижевск",callback_data="v-izhevske")
novosibirsk=InlineKeyboardButton("Новосибирск",callback_data="v-novosibirske")
sanktpeterburg=InlineKeyboardButton("Санкт-Петербург",callback_data="v-sankt-peterburge")
ekaterinburg=InlineKeyboardButton("Екатеринбург",callback_data="v-ekaterinburge")
kazan=InlineKeyboardButton("Казань",callback_data="v-kazani")
nizhnem=InlineKeyboardButton("Нижний Новгород",callback_data="v-nizhnem-novgorode")
krasnoyarsk=InlineKeyboardButton("Красноярск",callback_data="v-krasnoyarske")
chelyabinsk=InlineKeyboardButton("Челябинск",callback_data="v-chelyabinske")
samar=InlineKeyboardButton("Самара",callback_data="v-samare")
ufa=InlineKeyboardButton("Уфа",callback_data="v-ufe")
rostov=InlineKeyboardButton("Ростов На Дону",callback_data="v-rostove-na-donu")
omsk=InlineKeyboardButton("Омск",callback_data="v-omske")
krasnodar=InlineKeyboardButton("Краснодар",callback_data="v-krasnodare")
voronezh=InlineKeyboardButton("Воронеж",callback_data="v-voronezhe")
perm=InlineKeyboardButton("Пермь",callback_data="v-permi")
volgograd=InlineKeyboardButton("Волгоград",callback_data="v-volgograde")
saratov=InlineKeyboardButton("Саратов",callback_data="v-saratove")
tyumen=InlineKeyboardButton("Тюмень",callback_data="v-tyumeni")
tolyatt=InlineKeyboardButton("Тольяти",callback_data="v-tolyatti")
back = InlineKeyboardButton("Домой🏠",callback_data="back")
select_siti = InlineKeyboardMarkup(row_width=2).add(moscow, izhevsk,novosibirsk,sanktpeterburg,ekaterinburg,kazan,nizhnem,
krasnoyarsk,chelyabinsk,samar,ufa,omsk,krasnodar, voronezh,perm,volgograd,saratov,tyumen,tolyatt).add(rostov).add(back)


data=["v-moskve","v-izhevske","v-novosibirske","v-sankt-peterburge","v-ekaterinburge","v-kazani","v-nizhnem-novgorode","v-krasnoyarske","v-chelyabinske",
"v-samare","v-ufe","v-rostove-na-donu","v-omske","v-krasnodare","v-voronezhe","v-permi","v-volgograde","v-saratove","v-tyumeni","v-tolyatti","back"]

# 166

