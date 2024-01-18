from dotenv import load_dotenv
from os import getenv
from pathlib import Path

ENV_FILENAME = '.env'
ENV_PATH = Path.cwd().absolute().joinpath(ENV_FILENAME)

load_dotenv(ENV_PATH)

DB_USERNAME = getenv('DB_USERNAME', 'user')
DB_PASSWORD = getenv('DB_PASSWORD', 'user1234')
DB_PORT = getenv('DB_PORT', '3306')
DB_NAME = getenv('DB_NAME', 'db_1')
SQLALCHEMY_DATABASE_URI = f'mysql://{DB_USERNAME}:{DB_PASSWORD}@mysql:{DB_PORT}/{DB_NAME}'