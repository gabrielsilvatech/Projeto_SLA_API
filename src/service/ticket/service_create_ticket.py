from uuid import uuid4

from src.model.ticket.entity_ticket import DataTicket
from src.model.ticket.tb_ticket import Ticket
from src.model.ticket.status_ticket  import StatusTicket


class ServicesCreateTicket:
    
    @staticmethod
    def create_ticket(id_user: str, data_ticket: DataTicket) -> Ticket:
        return Ticket(
            _id = str(uuid4()),
            name = data_ticket.name,
            description = data_ticket.description,
            agency = data_ticket.agency,
            priority = data_ticket.agency,
            status_ticket = StatusTicket.OPEN,
            id_creator = id_user
        )
