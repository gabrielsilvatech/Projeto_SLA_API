from fastapi import APIRouter, Depends
from fastapi.security.http import HTTPAuthorizationCredentials

from src.controller.ticket.create_ticket import CreateTicket
from src.model.ticket.entity_ticket import DataTicket, ResponseCreateTicket
from src.service.autentic.service_autentic import ServiceAutenticUser


class RoutesTicket:

    route_ticket = APIRouter(tags=["TICKET"])
    
    @staticmethod
    @route_ticket.post("/create_ticket")
    def create_user(data:DataTicket, token: HTTPAuthorizationCredentials = Depends(ServiceAutenticUser.validate_token)) -> ResponseCreateTicket:
        return CreateTicket().create(data,token)
