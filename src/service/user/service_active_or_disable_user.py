from fastapi import HTTPException

from src.model.user.tb_user import User
from src.model.user.entity_user import PermissionCreateAndDisableUser
from src.model.user.user_status import UserStatus


class ServicesUpdateSttsUser:
    
    
    @staticmethod
    def valid_has_permission(user_requester: User|None) -> int:
        if user_requester is None:
            raise HTTPException(status_code=404, detail="Usuário não encontrado.")
        
        if user_requester.type.value not in [PermissionCreateAndDisableUser.ADMIN.value, PermissionCreateAndDisableUser.MANAGER.value, PermissionCreateAndDisableUser.DEVELOPER.value]:
            raise HTTPException(status_code=401, detail="Permissão negada.")
        
        return True
    
    @staticmethod
    def valid_existence_user(user_to_be_created:User|None):
        if user_to_be_created is None:
            raise HTTPException(status_code=409, detail="Não existe nenhum usuario registrado com este cpf.")
    
    @staticmethod  
    def toggle_status(current_status: UserStatus) -> UserStatus:
        if current_status == UserStatus.DESATIVADO:
            return UserStatus.ACTIVATE
        elif current_status == UserStatus.ACTIVATE:
            return UserStatus.DESATIVADO
        else:
            raise ValueError("Status inválido")