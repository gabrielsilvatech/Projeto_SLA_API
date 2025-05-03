from fastapi import HTTPException
from src.utilities.utility import Utility
from src.configs.database.connect_managerpayments import DbConnectionHandler
from src.model.ticket.tb_ticket import Ticket
from src.model.user.tb_user import User


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
            
    def list_tickets(self, skip: int, limit: int):
        with self as db:
            try:
                tickets = db.session.query(Ticket).offset(skip).limit(limit).all()
                return tickets
            
            except Exception as e:
                print(e)
                raise HTTPException(status_code=409, detail="Erro ao acessar banco de dados.")
    
    def find_user_by_id(self, id_user: str) -> User:
        with self as db:
            try:
                user = db.session.query(User).filter_by(_id=id_user).first()
                return user
            
            except:
                raise HTTPException(status_code=409, detail="Erro ao acessar banco de dados.")
