from aiogram import types

from filters import IsSubscriber
from loader import dp
from utils.db_api import quick_commands as commands
from utils.misk import rate_limit


@rate_limit(limit=3)
@dp.message_handler(IsSubscriber(), commands=['start'])
async def command_start(message: types.Message):
    args = message.get_args()
    print(args)
    new_args = await commands.check_args(args, message.from_user.id)
    print(new_args)
    try:
        user = await commands.select_user(message.from_user.id)
        if user.status == 'banned':
            await message.answer("You're banned")

    except Exception:
        await commands.add_user(user_id=message.from_user.id,
                                first_name=message.from_user.first_name,
                                last_name=message.from_user.last_name,
                                username=message.from_user.username,
                                status='active',
                                tokens=1000,
                                referal_id=int(new_args)
                                )

        await message.answer('You are successfully registered.\n'
                             'Write any message and the bot will reply to you.')

