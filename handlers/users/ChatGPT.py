import openai
from aiogram import types

from handlers.users.bot_referals import commands_ref
from handlers.users.inline_key_board import ikb_menu
from loader import dp
from data.config import OPEN_AI_TOKEN


from utils.db_api.quick_commands import select_user, update_token

openai.api_key = OPEN_AI_TOKEN


@dp.message_handler()
async def ChatGPT(message: types.Message):
    if message.text == '/referral':
        await commands_ref()
        pass
    else:
        user = await select_user(message.from_user.id)
        if user.tokens > 20:
            token_now = user.tokens - len(message.text)
            await update_token(message.from_user, token_now)
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=message.text,
                temperature=0.7,
                max_tokens=1000,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0

            )

            await message.answer(response["choices"][0]["text"], reply_markup=ikb_menu)
        else:
            await message.answer("You don't have enough tokens")