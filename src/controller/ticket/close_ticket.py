from fastapi.security.http import HTTPAuthorizationCredentials

from src.utilities.utility import Utility
from src.repository.ticket.ticket_repository import TicketRepository
from src.service.ticket.service_create_ticket import ServicesCreateTicket
from src.service.autentic.service_autentic import ServiceAutenticUser
from src.model.ticket.entity_ticket import CloseTicket, ResponseSuccess

class FinishTicket:
    
    def __init__(self) -> None:
        self.utiliti_autentic_user = ServiceAutenticUser
        self.services =  ServicesCreateTicket
        self.utilities = Utility
        self.ticket_repository = TicketRepository()
        
        
    def close(self, data_ticket: CloseTicket, token:HTTPAuthorizationCredentials) -> ResponseSuccess:
        self.ticket_repository.closed_ticket(data_ticket.id_ticket, data_ticket.status_ticket)
        return ResponseSuccess(success=True)
        
        
        