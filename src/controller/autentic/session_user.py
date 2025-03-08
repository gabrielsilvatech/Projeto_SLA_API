
from src.service.autentic.service_autentic import ServiceAutenticUser
from src.repository.user.user_repository import UserRepository
from src.model.user.entity_user import LoginUserOld


class Login:
    
    def __init__(self) -> None:
        self.services_autentic_user = ServiceAutenticUser
        self.user_repository = UserRepository()
        
    def try_login(self, user: LoginUserOld):
        response_repository_user = self.user_repository.find_user_by_login_old(user)
        self.services_autentic_user.validate_user(response_repository_user)
        self.services_autentic_user.validate_password_old(user, response_repository_user)
        token = self.services_autentic_user.create_token(response_repository_user)
        response = self.services_autentic_user.response_token(token,response_repository_user)
        return response
       