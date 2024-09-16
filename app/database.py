from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='../.env.development')

MARIADB_ROOT_PASSWORD = os.getenv('MARIADB_ROOT_PASSWORD')
MARIADB_DATABASE = os.getenv('MARIADB_DATABASE')

SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://root:{MARIADB_ROOT_PASSWORD}@localhost:3306/{MARIADB_DATABASE}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()
