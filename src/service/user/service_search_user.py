from fastapi import HTTPException

from src.model.user.tb_user import User
from src.model.user.entity_user import ResponseUser
from src.model.user.tb_user import User


class ServiceSearchUser:
    
    
    @staticmethod
    def validate_user(user: User | None) -> bool:
        if user is None:
            raise HTTPException(status_code = 404, detail = "Usuário não encontrado.")
        
        return True   
            
    @staticmethod
    def validate_response_search_user(search_user: User) -> ResponseUser:
        data_response = ResponseUser(
            ID = search_user.id,
            NAME = search_user.name,
            CPF = search_user.cpf,
            TYPE = search_user.type.name,
            LOGIN = search_user.login,
            EMAIL = search_user.email,
            AGENCY = search_user.agency,
            CREATE_USER = search_user.id_creator_user,
            SUPERVISOR = search_user.id_supervisor,
            STATUS_USER = search_user.status_user.name
        )
        return data_response
