from fastapi import HTTPException
from uuid import uuid4

from src.model.user.tb_user import User
from src.model.user.entity_user import PermissionCreateAndDisableUser
from src.model.agency.agency_type import AgencyType
from src.model.user.entity_user import BaseUser, ResponseCreateUser
from src.model.user.tb_user import User
from src.model.user.user_status  import UserStatus



class ServicesCreateUser:
    
    
    @staticmethod
    def validate_has_permission(user_requester: User|None) -> int:
        if user_requester is None:
            raise HTTPException(status_code=404, detail="Usuário não encontrado.")
        
        if user_requester.type.value not in [PermissionCreateAndDisableUser.ADMIN.value, PermissionCreateAndDisableUser.MANAGER.value, PermissionCreateAndDisableUser.DEVELOPER.value]:
            raise HTTPException(status_code=401, detail="Permissão negada.")
        
        return True
    
    @staticmethod
    def validate_doc_user(doc:str) -> bool:
        if doc != "CPF":
            raise HTTPException(status_code=409, detail="Documento inválido.")
        return True
    
    @staticmethod
    def validate_type_user(type: int) -> bool:
        if type in [5, 6]:
            return True
        
        return False
    
    @staticmethod
    def validate_whether_the_supervisor_or_not(user_to_be_created: BaseUser) -> None|int:
        if user_to_be_created.AGENCY == AgencyType.FULL_ACCESS:
            return None
        return user_to_be_created.AGENCY.value
    
    @staticmethod
    def validate_supervisor(supervisor: User | None) -> User:
        if supervisor is None:
            raise HTTPException(status_code = 404, detail = "Supervisor não encontrado.")
        
        return supervisor
    
    @staticmethod
    def validate_supervison(user_agency: int, supervisor_agency: int) -> bool:
        if supervisor_agency == 3:
            return True

        if user_agency != supervisor_agency:
            raise HTTPException(status_code=404, detail="Supervisor e o usuário não são da mesma carteira.")
        
        return True
        
    @staticmethod
    def validate_existence_user(user_to_be_created: User | None):
        if user_to_be_created is not None:
            raise HTTPException(status_code=409, detail="Já existe um usuario registrado com este cpf.")
            
    @staticmethod
    def mount_user_entity(id_user: str, base_user: BaseUser, id_supervisor: str | None, hash_password: bytes) -> User:
        user_insert = User(
            _id = str(uuid4()),
            name = base_user.NAME.title(),
            cpf = base_user.CPF,
            agency = base_user.AGENCY,
            type = base_user.TYPE,
            status_user = UserStatus.ACTIVATE,
            login = base_user.LOGIN,
            password = hash_password,
            email = base_user.EMAIL,
            id_supervisor = id_supervisor,
            id_creator_user = id_user
        )
        return user_insert
    
    @staticmethod
    def validate_response_create_user() -> ResponseCreateUser:
        return ResponseCreateUser(
            SUCCESS = True
        )