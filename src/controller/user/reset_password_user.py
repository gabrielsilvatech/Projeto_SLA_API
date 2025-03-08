from fastapi.security.http import HTTPAuthorizationCredentials

from src.repository.user.user_repository import UserRepository
from src.service.autentic.service_autentic import ServiceAutenticUser
from src.service.user.service_reset_password_user import ServiceResetPassword




class ResetPassword:
    
    def __init__(self) -> None:
        self.user_repository = UserRepository()
        self.utiliti_autentic_user = ServiceAutenticUser
        self.service_reset = ServiceResetPassword
    

    def reset(self,cpf_user_reset:str,token:HTTPAuthorizationCredentials) -> bool:
        user_id_token = self.utiliti_autentic_user.get_id_user_in_token(token)
        user_id = self.user_repository.find_user_by_id(user_id_token)
        self.service_reset.validate_has_permission(user_id)
        user_query = self.user_repository.find_user_by_cpf(cpf_user_reset)
        self.service_reset.validate_existence_user(user_query)
        self.user_repository.update_reset_password(cpf_user_reset,True)
        return True
        
        
        
        
        
        
        
        
        
    