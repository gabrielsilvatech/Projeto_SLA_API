from fastapi.security.http import HTTPAuthorizationCredentials

from src.utilities.utility import Utility
from src.repository.user.user_repository import UserRepository
from src.service.user.service_update_data_user import ServiceUpdateUser
from src.service.autentic.service_autentic import ServiceAutenticUser
from src.model.user.entity_user import DataUpdateUser


class UpdateDataUser:
    
    
    def __init__(self) -> None:
        self.utiliti_autentic_user = ServiceAutenticUser
        self.services =  ServiceUpdateUser
        self.utilities = Utility
        self.user_repository = UserRepository()
        
        
    def update(self,base_user: DataUpdateUser, token:HTTPAuthorizationCredentials) -> bool :
        user_id_token = self.utiliti_autentic_user.get_id_user_in_token(token)
        user_id = self.user_repository.find_user_by_id(user_id_token)
        self.services.validate_has_permission(user_id)
        user_query = self.user_repository.find_user_by_cpf(base_user.CPF)
        self.services.validate_existence_user(user_query)
        id_supervisor = self.user_repository.find_user_supervision_agency(base_user.AGENCY.value) if base_user.AGENCY else self.user_repository.find_user_supervision_agency(user_query.agency)
        base_user,id_supervisor_defined = self.services.mount_user(user_query,base_user,id_supervisor)
        self.user_repository.update_user(user_query,base_user,id_supervisor_defined)
        return True
        
        
        