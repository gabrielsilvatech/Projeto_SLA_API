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
    

class ResponseCreateTicket(BaseModel):
    success: bool
    
