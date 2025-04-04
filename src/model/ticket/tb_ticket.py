from sqlalchemy import Column, VARCHAR, Integer
from sqlalchemy.orm import  declarative_base
from typing import cast

from src.model.ticket.status_ticket import StatusTicket
from src.model.ticket.priority import Priority
from src.model.agency.agency_type import AgencyType

Base = declarative_base()

class Ticket(Base):
    
    __tablename__ = "tb_ticket"

    _id = Column("id", VARCHAR(255), primary_key=True, nullable=False)
    _name = Column("name", VARCHAR(200), nullable=False)
    _description = Column("description", VARCHAR(255), nullable=False)
    _agency = Column("agency", Integer, nullable=False)
    _priority = Column("priority", Integer, nullable=False)
    _status_ticket = Column("status_ticket", Integer, nullable=False)
    _id_creator = Column("id_creator", VARCHAR, nullable=False)

    
    @property
    def id(self) -> str:
        return cast(str, self._id)

    @property
    def name(self) -> str:
        return cast(str, self._name)
    
    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def description(self) -> str:
        return cast(str, self._description)
    
    @description.setter
    def description(self, value: str) -> None:
        self._description = value

    @property
    def agency(self) -> int:
        return cast(int, self._agency)
    
    @agency.setter
    def agency(self, value: AgencyType) -> None:
        self._agency = value.value

    @property
    def priority(self) -> Priority:
        return Priority(self._priority)

    @priority.setter
    def priority(self, value: Priority) -> None:
        self._priority = value.value
    
    @property
    def status_ticket(self) -> StatusTicket:
        return StatusTicket(self._status_ticket)

    @status_ticket.setter
    def status_ticket(self, value: StatusTicket) -> None:
        self._status_ticket = value.value

    @property
    def id_creator(self) -> str:
        return cast(str, self._id_creator)
    
    @id_creator.setter
    def id_creator(self, value: str) -> None:
        self._id_creator = value
