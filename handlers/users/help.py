from aiogram import types
from loader import dp
from utils.misk import rate_limit


@rate_limit(limit=3)
@dp.message_handler(text='/help')
async def command_help(message: types.Message):
    await message.answer('For questions, contact: @wasdxy')
