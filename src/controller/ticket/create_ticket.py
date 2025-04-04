from fastapi.security.http import HTTPAuthorizationCredentials

from src.utilities.utility import Utility
from src.repository.ticket.ticket_repository import TicketRepository
from src.service.ticket.service_create_ticket import ServicesCreateTicket
from src.service.autentic.service_autentic import ServiceAutenticUser
from src.model.ticket.entity_ticket import DataTicket, ResponseCreateTicket

class CreateTicket:
    
    def __init__(self) -> None:
        self.utiliti_autentic_user = ServiceAutenticUser
        self.services =  ServicesCreateTicket
        self.utilities = Utility
        self.ticket_repository = TicketRepository()
        
        
    def create(self, data_ticket: DataTicket, token:HTTPAuthorizationCredentials) -> ResponseCreateTicket:
        user_id = self.utiliti_autentic_user.get_id_user_in_token(token)
        data_insert = self.services.create_ticket(user_id, data_ticket)
        self.ticket_repository.insert_ticket(data_insert)
        return ResponseCreateTicket(success=True)
        
        
        