from fastapi import HTTPException
from src.utilities.utility import Utility
from src.configs.database.connect_managerpayments import DbConnectionHandler
from src.model.user.tb_user import User
from src.model.user.entity_user import LoginUser, LoginUserOld
from src.model.user.user_status  import UserStatus
from src.model.user.entity_user import DataUpdateUser
from src.model.user.user_type import UserType

class UserRepository(DbConnectionHandler):
    def __init__(self) -> None:
        super().__init__()
        self.update_attribute = Utility.update_attribute
    
    def find_user_by_id(self, id_user: str) -> User:
        with self as db:
            try:
                user = db.session.query(User).filter_by(_id=id_user).first()
                return user
            
            except:
                raise HTTPException(status_code=409, detail="Erro ao acessar banco de dados.")
    
    def find_user_by_login(self, user:LoginUser) -> User:
        with self as db:
            try:
                user = db.session.query(User).filter_by(_login=user.login).first()
                return user
            
            except:
                raise HTTPException(status_code=409, detail="Erro ao acessar banco de dados.")
            
    def find_user_by_login_old(self, user:LoginUserOld) -> User:
        with self as db:
            try:
                user = db.session.query(User).filter_by(_login=user.login).first()
                return user
            
            except Exception as e:
                print(e)
                raise HTTPException(status_code=409, detail="Erro ao acessar banco de dados.")
            
    def find_user_by_name_login(self, login_name:str) -> User:
        with self as db:
            try:
                user = db.session.query(User).filter_by(_login = login_name).first()
                return user
            
            except:
                raise HTTPException(status_code=409, detail="Erro ao acessar banco de dados.")
    
    def find_user_supervision_agency(self,agency:int) -> User:
        with self as db:
            try:
                user = db.session.query(User).filter_by(_agency = agency,_type = UserType.SUPERVISOR.value).first()
                return user
            
            except:
                raise HTTPException(status_code=409, detail="Erro ao acessar banco de dados.")
            
    def find_user_by_cpf(self, cpf:str) -> User:
        with self as db:
            try:
                user = db.session.query(User).filter_by(_cpf = cpf).first()
                return user
            
            except:
                raise HTTPException(status_code=409, detail="Erro ao acessar banco de dados.")
            
    def insert_user(self, user_insert:User):
        with self as db:
            try:
                db.session.add(user_insert)
                db.session.commit()

            except Exception as e:
                print(e)
                db.session.rollback()
                raise HTTPException(status_code=409, detail="Erro ao acessar banco de dados.")
    
    def update_data_user(self, cpf: str,status:UserStatus):
        with self as db:
            user = db.session.query(User).filter_by(_cpf =cpf).first()
            
            if user is not None:
                try:
                    user.status_user = status
                    db.session.commit()
                    
                except:
                    raise HTTPException(status_code=500, detail="Erro ao tentar atualizar o status do usuario.")
                    
            else:
                raise HTTPException(status_code=404, detail="Usuario não encontrato.")
    
    def update_user(self, user_bd: User, user_att: DataUpdateUser,id_supervisor:str|None):
        with self as db:
            try:
                user = db.session.merge(user_bd)
                if user_att.NAME:
                    user.name = self.update_attribute(user_bd.name, user_att.NAME.strip().title()) 
                if user_att.EMAIL:
                    user.email = self.update_attribute(user_bd.email, user_att.EMAIL.strip()) 
                if user_att.AGENCY:  
                    user.agency = self.update_attribute(user_bd.agency, user_att.AGENCY) 
                    user.id_supervisor = self.update_attribute(user_bd.id_supervisor,id_supervisor)
                    
                if user_att.TYPE:
                    user.type = self.update_attribute(user_bd.type,user_att.TYPE)
             
                    
                db.session.commit()
                
            except:
                db.session.rollback()
                raise HTTPException(status_code=409, detail="Erro ao acessar banco de dados.")
            
    
    
            
    def update_reset_password(self,cpf: str,change:bool):
        with self as db:
            user = db.session.query(User).filter_by(_cpf =cpf).first()
            
            if user is not None:
                try:
                    user.password_reset = change
                    user.password = ''
                    db.session.commit()
                    
                except:
                    raise HTTPException(status_code=500, detail="Erro ao tentar resetar a senha do usuario")
                    
            else:
                raise HTTPException(status_code=404, detail="Usuario não encontrato.")
            
            
    def update_password(self,cpf: str,password:str):
        with self as db:
            user = db.session.query(User).filter_by(_cpf =cpf).first()
            
            if user is not None:
                try:
                    user.password_reset = False
                    user.password = password
                    db.session.commit()
                    
                except:
                    raise HTTPException(status_code=500, detail="Erro ao tentar alterar a senha do usuario")
                    
            else:
                raise HTTPException(status_code=404, detail="Usuario não encontrato.")