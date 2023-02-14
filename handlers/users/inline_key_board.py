from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from loader import bot
from loader import dp

ikb_menu = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Reset dialog', callback_data='forget dialogue')

                                    ]
                                ])


@dp.callback_query_handler(text="forget dialogue")
async def inlines(callback: types.CallbackQuery):
    await bot.send_message(callback.message.chat.id, 'Диалог сброшен')