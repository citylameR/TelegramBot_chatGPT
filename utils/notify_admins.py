import logging
from aiogram import Dispatcher
from data.config import admins


async def on_startup_notify(dp: Dispatcher):
    for admin in admins:
        try:
            test = 'Бот запущен, и готов к работе'
            await dp.bot.send_message(chat_id=admin, text=test)
        except Exception as err:
            logging.exception(err)