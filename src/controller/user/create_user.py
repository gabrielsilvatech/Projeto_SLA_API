from fastapi.security.http import HTTPAuthorizationCredentials

from src.utilities.utility import Utility
from src.repository.user.user_repository import UserRepository
from src.service.user.service_create_user import ServicesCreateUser
from src.service.autentic.service_autentic import ServiceAutenticUser
from src.model.user.entity_user import BaseUser, ResponseCreateUser

class CreateUser:
    
    
    def __init__(self) -> None:
        self.utiliti_autentic_user = ServiceAutenticUser
        self.services =  ServicesCreateUser
        self.utilities = Utility
        self.user_repository = UserRepository()
        
        
    def create(self,base_user: BaseUser, token:HTTPAuthorizationCredentials) -> ResponseCreateUser:
        user_id_token = self.utiliti_autentic_user.get_id_user_in_token(token)
        user_id = self.user_repository.find_user_by_id(user_id_token)
        self.services.validate_has_permission(user_id)
        type_doc = self.utilities.validation_doc(base_user.CPF)
        self.services.validate_doc_user(type_doc)
        user_query = self.user_repository.find_user_by_cpf(base_user.CPF)
        self.services.validate_existence_user(user_query)
        name_login = self.user_repository.find_user_by_name_login(base_user.LOGIN)
        self.services.validate_existence_user(name_login)
        need_supervisor = self.services.validate_type_user(base_user.TYPE.value)
        if need_supervisor:
            supervisor_query = self.user_repository.find_user_by_id(base_user.ID_SUPERVISOR) #type: ignore
            supervisor = self.services.validate_supervisor(supervisor_query)
            self.services.validate_supervison(base_user.AGENCY.value, supervisor.agency)

        hash_password = self.utilities.create_hash_password(base_user.PASSWORD)#type: ignore
        data_insert = self.services.mount_user_entity(user_id.id, base_user, base_user.ID_SUPERVISOR, hash_password)#type: ignore
        self.user_repository.insert_user(data_insert)
        response = self.services.validate_response_create_user()
        return response
        
        
        