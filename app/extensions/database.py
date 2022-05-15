from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
import os


class MyDatabase():
    def __init__(self, path: str = os.getenv('DATABASE_PATH'), name: str = os.getenv('DATABASE_NAME')):
        self.path = path
        self.name = name
    
    def get_engine(self):
        return create_engine(f'sqlite+pysqlite:///{self.path}{self.name}.db')

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