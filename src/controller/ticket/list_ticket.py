from src.utilities.utility import Utility
from src.repository.ticket.ticket_repository import TicketRepository
from src.service.ticket.service_create_ticket import ServicesCreateTicket
from src.service.autentic.service_autentic import ServiceAutenticUser
from src.model.ticket.entity_ticket import DataSearchTicket, ResponseListTicket
from src.model.agency.agency_type import AgencyType
from src.model.ticket.status_ticket import StatusTicket
from src.model.ticket.priority import Priority

class ListTicket:
    
    def __init__(self) -> None:
        self.list_tickets: list[ResponseListTicket] = []
        self.utiliti_autentic_user = ServiceAutenticUser
        self.services =  ServicesCreateTicket
        self.utilities = Utility
        self.ticket_repository = TicketRepository()
        
        
    def list(self, data_ticket: DataSearchTicket) -> list[ResponseListTicket]:
        tickets = self.ticket_repository.list_tickets(data_ticket.skip, data_ticket.limit)
        for ticket in tickets:
            user = self.ticket_repository.find_user_by_id(ticket.id_creator)
            list_name = user.name.split(" ")
            name_user = f"{list_name[0]} {list_name[-1]}"
            self.list_tickets.append(
                ResponseListTicket(
                    title = ticket.name,
                    description = ticket.description,
                    agency = AgencyType(ticket.agency).name,
                    priority = Priority(ticket.priority).name,
                    status_ticket = StatusTicket(ticket.status_ticket).name,
                    creator = name_user
                )
            )
        return self.list_tickets
        
        
        