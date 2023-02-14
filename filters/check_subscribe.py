from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from aiogram.dispatcher.handler import CancelHandler
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data import config
from loader import bot, dp


class IsSubscriber(BoundFilter):
    async def check(self, message: types.Message):
        for chat_id in '@TGenNews':
            sub = await bot.get_chat_member(chat_id='@TGenNews', user_id=message.from_user.id)
            if sub.status != types.ChatMemberStatus.LEFT:
                return True
        else:
            markup = InlineKeyboardMarkup(row_width=1,
                                          inline_keyboard=[
                                              [
                                                  InlineKeyboardButton(
                                                      text='Telegram Channel',
                                                      url='https://t.me/+7GBNc47jt4hhNGNi'
                                                  )
                                              ]
                                          ])
            await dp.bot.send_message(chat_id=message.from_user.id,
                                      text=f'Subscribe to the Telegram Channel and try again',
                                      reply_markup=markup
                                      )
            return CancelHandler()