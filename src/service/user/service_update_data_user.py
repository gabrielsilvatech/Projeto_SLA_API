from fastapi import HTTPException



from src.model.user.entity_user import PermissionCreateAndDisableUser
from src.model.user.entity_user import DataUpdateUser
from src.model.user.tb_user import User
from src.model.agency.agency_type import AgencyType

from src.model.user.user_type import UserType




class ServiceUpdateUser:
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
    def validate_existence_user(user_to_be_created: User | None):
        if user_to_be_created is None:
            raise HTTPException(status_code=409, detail="Nao existe nenhum usuario registrado com este cpf.")
        
            
    @staticmethod
    def mount_user(user_bd:User,user_att:DataUpdateUser,id_supervisor:str|None) -> tuple[DataUpdateUser,str|None]:
        
                
        if user_att.AGENCY and not user_att.TYPE :
            if  user_att.AGENCY == AgencyType.FULL_ACCESS:
                id_supervisor = id_supervisor
                id_supervisor = None
            
            if  user_att.AGENCY == AgencyType.FULL_ACCESS and user_bd.type.value not in [UserType.DEVELOPER.value,UserType.ADMIN.value,UserType.MANAGER.value]:
                raise HTTPException(status_code=400,detail='Este tipo de usuario não pode ter acesso total. Atualize o tipo do usuario.')
            
            if user_bd.type.value in  [UserType.DEVELOPER.value,UserType.ADMIN.value,UserType.MANAGER.value] and  user_att.AGENCY != AgencyType.FULL_ACCESS:
                raise HTTPException(status_code=400,detail='A carteira deste usuario só pode ser trocada mediante outro Tipo de usuario.')
            
     
        if user_att.TYPE:
            if user_att.TYPE.value in [UserType.DEVELOPER.value,UserType.ADMIN.value,UserType.MANAGER.value]:
                user_att.AGENCY = AgencyType.FULL_ACCESS
                id_supervisor = id_supervisor 
                id_supervisor = None
            
            elif user_att.TYPE.value in [UserType.SUPERVISOR.value]:
                if not user_att.AGENCY:
                    raise HTTPException(status_code=400,detail='É preciso especificar uma carteira para definir este tipo de usuario.')
                    
                id_supervisor = id_supervisor 
                id_supervisor = None
            
            elif user_att.TYPE.value in [UserType.OPERATOR.value, UserType.OPERATOR_MATTRESS.value]:
                if not id_supervisor:
                    raise HTTPException(status_code=400,detail='Supervisor da carteira não encontrado. Contate os Administradores do sistema.')
                if not user_att.AGENCY or user_att.AGENCY == AgencyType.FULL_ACCESS:
                    raise HTTPException(status_code=400,detail='É preciso especificar uma carteira para definir este tipo de usuario')
    
        return user_att,id_supervisor
