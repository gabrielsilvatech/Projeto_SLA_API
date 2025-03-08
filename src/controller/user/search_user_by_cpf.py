from fastapi.security.http import HTTPAuthorizationCredentials

from src.service.user.service_search_user import ServiceSearchUser
from src.service.autentic.service_autentic import ServiceAutenticUser
from src.repository.user.user_repository import UserRepository
from src.model.user.entity_user import ResponseUser


class SearchUserByCpf:
    
    def __init__(self, token: HTTPAuthorizationCredentials) -> None:
        self.id_user = ServiceAutenticUser.get_id_user_in_token(token)
        self.user_repository = UserRepository()
        self.service_user = ServiceSearchUser
        
    def search(self, user_cpf: str) -> ResponseUser:
        user = self.user_repository.find_user_by_id(self.id_user)
        self.service_user.validate_user(user)
        user_search = self.user_repository.find_user_by_cpf(user_cpf)
        self.service_user.validate_user(user_search)
        response_user = self.service_user.validate_response_search_user(user_search)
        return response_user