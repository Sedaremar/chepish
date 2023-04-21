from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
import sqlite3
import sys
sys.path.append(r"E:\bot_sadar")
import config


conn = sqlite3.connect(r"E:\bot_sadar\starts\data_base.db")
# conn = sqlite3.connect(":memory:")
cur = conn.cursor()


bot = Bot(token=config.TOKEN,parse_mode='HTML')
dp = Dispatcher(bot,storage=MemoryStorage())

class States(StatesGroup):  # Создаём состояния
    INPUT_LOC = State()
    MENU = State()
    SETTINGS = State()
    SELECT_GOR = State()
    SELECT_VGOR = State()

    TEXT_REMINDED = State()
    TIME_REMINDED = State()

    REVERS_TEXT = State()

    GAMES = State()
