import os
import dotenv

dotenv.load_dotenv()

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))
OPEN_AI_TOKEN = str(os.getenv('OPEN_AI_TOKEN'))


ip = os.getenv('ip')
PGUSER = str(os.getenv('PGUSER'))
PGPASSWORD = str(os.getenv('PGPASSWORD'))
DATABASE = str(os.getenv('DATABASE'))
PAYMENTS_TOKEN = str(os.getenv('PAYMENTS_TOKEN'))

POSTGRES_URI = f'postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}'
admins = [
    791108425
]


