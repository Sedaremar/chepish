from aiogram.utils import executor

from helps import bot, dp, conn, cur
import sys
sys.path.append(r"E:\bot_sadar")
from user.menu.main import user_register_handler
from user.currenc.main import currenc_register_handler
from user.weather.main import weather_register_handler
from handler_2 import handler2
from user.settings.main import set_register_handler
from user.reminder.main import reminder_timer_register
from user.horoscope.main import horoscops_register_handler

from user.vostochn_horoscop.main import vostok_horoscop_register
from user.cripta.main import cripto_currency_register
from user.games.main import game_register_handler


cur.execute("""CREATE TABLE IF NOT EXISTS user(
id TEXT,
coins INT,
remind TEXT
);""")




user_register_handler(dp)
currenc_register_handler(dp)
weather_register_handler(dp)
set_register_handler(dp)
reminder_timer_register(dp)
horoscops_register_handler(dp)
cripto_currency_register(dp)
vostok_horoscop_register(dp)
game_register_handler(dp)












if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)