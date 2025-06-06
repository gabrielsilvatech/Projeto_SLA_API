from pydantic import BaseModel

from src.model.agency.agency_type import AgencyType
from src.model.ticket.status_ticket import StatusTicket
from src.model.ticket.priority import Priority

class DataTicket(BaseModel):
    name: str
    description: str
    agency: AgencyType
    priority: Priority    
    status_ticket: StatusTicket
    id_creator: str


class DataSearchTicket(BaseModel):
    skip: int = 0
    limit: int = 15


class ResponseCreateTicket(BaseModel):
    success: bool
    

class ResponseSuccess(BaseModel):
    success: bool


class ResponseListTicket(BaseModel):
    title: str
    description: str
    agency: str
    priority: str    
    status_ticket: str
    creator: str
    id: str
    

class CloseTicket(BaseModel):
    id_ticket: str   
    status_ticket: StatusTicket