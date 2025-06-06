from fastapi import APIRouter, Depends
from fastapi.security.http import HTTPAuthorizationCredentials

from src.controller.ticket.create_ticket import CreateTicket
from src.controller.ticket.list_ticket import ListTicket
from src.controller.ticket.close_ticket import FinishTicket
from src.model.ticket.entity_ticket import DataTicket, DataSearchTicket, ResponseCreateTicket, ResponseListTicket, CloseTicket, ResponseSuccess
from src.service.autentic.service_autentic import ServiceAutenticUser


class RoutesTicket:

    route_ticket = APIRouter(tags=["TICKET"])
    
    @staticmethod
    @route_ticket.post("/create_ticket")
    def create_user(data:DataTicket, token: HTTPAuthorizationCredentials = Depends(ServiceAutenticUser.validate_token)) -> ResponseCreateTicket:
        return CreateTicket().create(data,token)
    
    @staticmethod
    @route_ticket.post("/list_tickets")
    def list_tickets(data:DataSearchTicket, token: HTTPAuthorizationCredentials = Depends(ServiceAutenticUser.validate_token)) -> list[ResponseListTicket]:
        return ListTicket().list(data)
    
    @staticmethod
    @route_ticket.post("/close_ticket")
    def close_ticket(data:CloseTicket, token: HTTPAuthorizationCredentials = Depends(ServiceAutenticUser.validate_token)) -> ResponseSuccess:
        return FinishTicket().close(data,token)
