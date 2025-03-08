from src.repository.user.user_repository import UserRepository
from fastapi.security.http import HTTPAuthorizationCredentials
from src.service.user.service_active_or_disable_user import ServicesUpdateSttsUser
from src.service.autentic.service_autentic import ServiceAutenticUser
from src.utilities.utility import Utility


class ActiveOrDisableUser:
    
    
    def __init__(self) -> None:
        self.utiliti_autentic_user = ServiceAutenticUser
        self.services =  ServicesUpdateSttsUser
        self.utilities = Utility
        self.user_repository = UserRepository()
        
        
    def update(self,cpf_user_disable:str, token:HTTPAuthorizationCredentials):
        user_id_token = self.utiliti_autentic_user.get_id_user_in_token(token)
        user_requester = self.user_repository.find_user_by_id(user_id_token)
        self.services.valid_has_permission(user_requester)
        response_user_repository = self.user_repository.find_user_by_cpf(cpf_user_disable)
        self.services.valid_existence_user(response_user_repository)
        stts = self.services.toggle_status(response_user_repository.status_user)
        self.user_repository.update_data_user(cpf_user_disable,stts)
        return True