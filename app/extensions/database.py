from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
import os


class MyDatabase():
    def __init__(self, host: str = os.getenv('DATABASE_HOST'),
                 port: str = os.getenv('DATABASE_PORT'),
                 user: str = os.getenv('DATABASE_USER'),
                 password: str = os.getenv('DATABASE_PASSWORD'),
                 dbname: str = os.getenv('DATABASE_NAME')):

        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.dbname = dbname

    def get_engine(self):
        return create_engine(f'postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}')

    def get_base(self):
        Base = declarative_base()
        return Base

    def get_session(self):
        try:
            MySession = Session(
                autocommit=False, autoflush=False, bind=self.get_engine())
            return MySession
        except Exception as e:
            raise e
        finally:
            MySession.close()


myDatabase = MyDatabase()
Base = myDatabase.get_base()