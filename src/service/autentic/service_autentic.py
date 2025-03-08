import jwt
import bcrypt
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv

from fastapi.security.http import HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer

from src.model.user.tb_user import User
from src.model.user.user_status import UserStatus
from src.model.user.entity_user import LoginUser, LoginUserOld
from src.model.agency.agency_type import AgencyType


class ServiceAutenticUser:
    load_dotenv()
    secret_key = "JurCobSisForIcr"
    
    @classmethod
    def validate_password(cls, user: LoginUser, password_user: User) -> bool:
        stored_password_bytes = password_user.password.encode('utf-8')
        password = bcrypt.checkpw(user.password.encode('utf-8'), stored_password_bytes)
        if not password:
            raise HTTPException(status_code=401,detail="Senha incorreta.")
        else:
            return True
        
    @classmethod
    def validate_password_old(cls, user: LoginUserOld, password_user: User) -> bool:
        stored_password_bytes = password_user.password.encode('utf-8')
        password = bcrypt.checkpw(user.password.encode('utf-8'), stored_password_bytes)
        if not password:
            raise HTTPException(status_code=401,detail="Senha incorreta.")
        else:
            return True

    @classmethod
    def create_token(cls,user:User) -> str:   
        payload = { # type: ignore
            'id': user.id,
            'username': user.login,
            'role': user.role,
            'exp': datetime.now(timezone.utc) + timedelta(minutes=120)
        } 
        token = jwt.encode(payload, cls.secret_key, algorithm='HS256') # type: ignore
        return token

    @classmethod
    def validate_token(cls, token: HTTPAuthorizationCredentials = Depends(HTTPBearer())) -> HTTPAuthorizationCredentials:
        try:
            decoded_token = jwt.decode(token.credentials, cls.secret_key, algorithms=['HS256']) # type: ignore
            expiracao = decoded_token['exp']
            data_expiracao = datetime.fromtimestamp(expiracao, timezone.utc)
            data_atual = datetime.now(timezone.utc)
            if data_atual < data_expiracao:
                return token
            else:
                raise HTTPException(status_code=401, detail="Token expirado.")

        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token expirado.")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Token inválido.")

    @classmethod
    def validate_user(cls,user:User|None):
        if user is None:
            raise HTTPException(status_code=401, detail="Login incorreto.")
            
        if user.status_user == UserStatus.DESATIVADO:
            raise HTTPException(status_code=401, detail="Usuário Inativo.")
    
    @classmethod
    def response_token(cls,token:str,user:User): # type: ignore
        dict_response:dict[str,str] = {"Authorization": token, # type: ignore
                "data_user":{
                        "id":  user.id,
                        "type": user.type.name,
                        "login":  user.login,
                        "agency": AgencyType(user.agency).name,
                    }
                }
        return dict_response
    
    @classmethod
    def get_id_user_in_token(cls, token: HTTPAuthorizationCredentials) -> str:
        decoded = jwt.decode(token.credentials, cls.secret_key, algorithms=['HS256']) # type: ignore
        user_id = str(decoded.get("id"))
        return user_id 
    
    
    @staticmethod
    def create_hash_password(password:str):
        salt = bcrypt.gensalt()
        hash_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hash_password
    