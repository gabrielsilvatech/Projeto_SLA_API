from fastapi import APIRouter, Depends
from fastapi.security.http import HTTPAuthorizationCredentials

from src.controller.user.create_user import CreateUser,ResponseCreateUser
from src.controller.user.active_or_disable_user import ActiveOrDisableUser
from src.controller.user.reset_password_user import ResetPassword
from src.controller.user.search_user_by_cpf import SearchUserByCpf
from src.controller.user.update_data_user import UpdateDataUser, DataUpdateUser
from src.model.user.entity_user import BaseUser, ResponseUser
from src.service.autentic.service_autentic import ServiceAutenticUser


class RoutesUser:

    route_user = APIRouter(tags=["USERS"])
    
    @staticmethod
    @route_user.post("/create_user")
    def create_user(user_create_json:BaseUser, token: HTTPAuthorizationCredentials = Depends(ServiceAutenticUser.validate_token)) -> ResponseCreateUser:
        response_create_user = CreateUser().create(user_create_json,token)
        return response_create_user
    
    @staticmethod
    @route_user.put("/active_or_disable_user")
    def active_or_disable_user(cpf_user_update:str, token: HTTPAuthorizationCredentials = Depends(ServiceAutenticUser.validate_token)) -> bool:
        response = ActiveOrDisableUser().update(cpf_user_update,token)
        return response
    
    @staticmethod
    @route_user.put("/reset_password")
    def reset_password(cpf_user_reset:str, token: HTTPAuthorizationCredentials = Depends(ServiceAutenticUser.validate_token)) -> bool:
        response_reset = ResetPassword().reset(cpf_user_reset,token)
        return response_reset

    @staticmethod
    @route_user.put("/update_data_user")
    def update_data_user(data:DataUpdateUser, token: HTTPAuthorizationCredentials = Depends(ServiceAutenticUser.validate_token)) -> bool:
        response = UpdateDataUser().update(data,token)
        return response

    @staticmethod
    @route_user.get("/search_user_by_cpf")
    def search_user_by_cpf(data:str, token: HTTPAuthorizationCredentials = Depends(ServiceAutenticUser.validate_token)) -> ResponseUser:
        response_search_user_by_cpf = SearchUserByCpf(token).search(data)
        return response_search_user_by_cpf