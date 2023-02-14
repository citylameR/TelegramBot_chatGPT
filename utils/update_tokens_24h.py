from utils.db_api.schemas.user import User
from asyncio import sleep


async def update_all_token():
    while True:
        await sleep(60 * 60 * 24)
        users = await User.query.where(User.tokens < 500).gino.all()
        for i in range(len(users)):
            await users[i].update(tokens=500).apply()
