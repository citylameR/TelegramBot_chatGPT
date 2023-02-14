from aiogram import Dispatcher

from .check_subscribe import IsSubscriber


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsSubscriber)
