from fastapi import HTTPException

from src.model.user.tb_user import User
from src.model.user.entity_user import PermissionCreateAndDisableUser



class ServiceResetPassword:
    
    @staticmethod
    def validate_has_permission(user_requester: User|None) -> bool:
        if user_requester is None:
            raise HTTPException(status_code=404, detail="Usuário não encontrado.")
        
        if user_requester.type.value not in PermissionCreateAndDisableUser:
            raise HTTPException(status_code=401, detail="Permissão negada.")
        
        return True
    
    
    @staticmethod
    def validate_existence_user(user: User|None) -> bool:
        if user is None:
            raise HTTPException(status_code=404, detail="Usuário não encontrado.")

        
        return True
    
    