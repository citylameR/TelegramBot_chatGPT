from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data import config

from utils.db_api.db_gino import db

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)


dp = Dispatcher(bot, storage=MemoryStorage())

__all__ = ['bot', 'dp', 'db']
