from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.user import User


async def add_user(user_id: int, first_name: str, last_name: str, username: str, status: str, tokens: int,
                   referal_id: int):
    try:
        user = User(user_id=user_id, first_name=first_name, last_name=last_name, username=username, status=status,
                    tokens=tokens, referal_id=referal_id)
        await user.create()
    except UniqueViolationError:
        print('Пользователь не добавлен')


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def count_users():
    count = await db.func.count(User.user_id).gino.scalar()
    return count


async def select_user(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user


async def update_user(user_id, status):
    user = await select_user(user_id)
    await user.update(status=status).apply()


async def update_token(user_id, new_token):
    user = await select_user(user_id)
    await user.update(tokens=new_token).apply()


async def count_refs(user_id):
    refs = await User.query.where(User.referal_id == user_id).gino.all()
    return len(refs)


async def check_args(args, user_id: int):
    if args == '':
        args = '0'
        return args

    elif not args.isnumeric():
        args = '0'
        return args

    elif args.isnumeric():
        if int(args) == user_id:
            args = '0'
            return args

        elif await select_user(user_id=int(args)) is None:
            args = '0'
            return args

        else:
            args = str(args)
            return args

    else:
        args = '0'
        return args
