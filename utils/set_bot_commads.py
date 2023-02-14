from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Старт'),
        types.BotCommand('account', 'Аккаунт'),
        types.BotCommand('help', 'Помощь'),
        types.BotCommand('referrals', 'Реферальная система')
    ])
