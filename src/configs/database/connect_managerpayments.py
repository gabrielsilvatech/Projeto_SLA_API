import os
from typing import Any
from dotenv import load_dotenv
from urllib.parse import quote_plus
from sqlalchemy.orm import sessionmaker
from sqlalchemy import  create_engine, Engine


class DbConnectionHandler:

    def __init__(self) -> None:
        load_dotenv()
        senha_database = os.getenv('MYSQL_PASSWORD')
        senha_database = quote_plus(senha_database) # type: ignore
        name_database = os.getenv('MYSQL_DB')
        host_database = os.getenv('MYSQL_HOST')
        user_database = os.getenv('MYSQL_USER')
        self.connection_string = f"mysql+mysqlconnector://{user_database}:{senha_database}@{host_database}:3306/{name_database}"
        self._engine = self.create_database_engine()
        self.Session = None

    def create_database_engine(self) -> Engine:
        engine = create_engine(self.connection_string)
        return engine

    @property
    def engine(self) -> Engine:
        return self._engine

    def __enter__(self):
        session_make = sessionmaker(bind=self._engine)
        self.session = session_make()
        return self
    
    def __exit__(self, exc_type:None|Any, exc_val:None|Any, exc_tb:None|Any):
        self.session.close()