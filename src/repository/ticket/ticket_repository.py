from fastapi import HTTPException
from src.utilities.utility import Utility
from src.configs.database.connect_managerpayments import DbConnectionHandler
from src.model.ticket.tb_ticket import Ticket


class TicketRepository(DbConnectionHandler):
    def __init__(self) -> None:
        super().__init__()
        self.update_attribute = Utility.update_attribute
       
    def insert_ticket(self, ticket:Ticket):
        with self as db:
            try:
                db.session.add(ticket)
                db.session.commit()

            except Exception as e:
                print(e)
                db.session.rollback()
                raise HTTPException(status_code=409, detail="Erro ao acessar banco de dados.")
