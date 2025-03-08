from fastapi import APIRouter

from src.model.user.entity_user import LoginUser, LoginUserOld#type:ignore
from src.controller.autentic.session_user import Login


class RoutesLogin:

    route_login = APIRouter(tags=["LOGIN"])
    
    @staticmethod 
    @route_login.post("/login_user")
    def login_user(login: LoginUserOld):
        instance_login = Login()
        response_login = instance_login.try_login(login)
        return response_login