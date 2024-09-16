from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from gemma import llm
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='../../.env.development')

MARIADB_ROOT_PASSWORD = os.getenv('MARIADB_ROOT_PASSWORD')
MARIADB_DATABASE = os.getenv('MARIADB_DATABASE')

SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://root:{MARIADB_ROOT_PASSWORD}@localhost:3306/{MARIADB_DATABASE}'

db = SQLDatabase.from_uri(SQLALCHEMY_DATABASE_URL, sample_rows_in_table_info=2)
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)