from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import  declarative_base
from typing import cast

Base = declarative_base()


class Agency(Base):
    
    __tablename__ = 'tb_agency'
    
    _id = Column("ID", Integer, primary_key=True)
    _agency_name = Column("AGENCY_NAME", String(50), nullable=False)

    @property
    def id(self) -> int:
        return cast(int, self._id)
    
    @property
    def agency_name(self) -> str:
        return cast(str, self._agency_name)
    
    @agency_name.setter
    def agency_name(self, value: str) -> None:
        self._agency_name = value