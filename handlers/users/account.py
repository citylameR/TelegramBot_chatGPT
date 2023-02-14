from aiogram import types


from loader import dp
from utils.db_api import quick_commands as commands
from utils.misk import rate_limit


@rate_limit(limit=3)
@dp.message_handler(text='/account')
async def command_account(message: types.Message):
    count_refs = await commands.count_refs(message.from_user.id)
    user = await commands.select_user(message.from_user.id)
    await message.answer(f'Count of tokens: {user.tokens} \n'
                         f'Number of referrals: {count_refs}\n'
                         'Support the author:\n'
                         '<code>0xAe55b8993F30cC74B3670d7f39D92aD45D560477</code>'
                        )
