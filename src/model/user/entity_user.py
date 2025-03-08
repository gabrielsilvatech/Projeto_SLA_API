from pydantic import BaseModel,Field
from enum import Enum
from typing import Optional

from src.model.user.user_type import UserType
from src.model.agency.agency_type import AgencyType


class BaseUser(BaseModel):
    NAME: str
    CPF: str  = Field(...,pattern=r'^\d{11}$') 
    LOGIN: str
    PASSWORD: str
    EMAIL: str = Field(..., pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')    
    AGENCY: AgencyType
    TYPE: UserType
    ID_SUPERVISOR: str | None
    

class DataUpdateUser(BaseModel):
    CPF: str  = Field(...,pattern=r'^\d{11}$') 
    NAME: Optional[str]
    EMAIL: Optional[str] = Field(..., pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')    
    AGENCY:  Optional[AgencyType]
    TYPE : Optional[UserType]


class LoginUser(BaseModel):
    login: str
    password: str
    change_password:bool


class LoginUserOld(BaseModel):
    login: str
    password: str


class PutUser(BaseModel):
    ID_USER_SOLICITANTE: int
    ID_USER_ATUALIZAR: int
    NAME: str | None 
    EMAIL: str| None  
    AGENCY: int | None
    TYPE: int | None
    ID_SUPERVISOR: int | None   


class ResponseUser(BaseModel):
    ID: str
    NAME: str
    CPF: str
    TYPE: str
    LOGIN: str
    EMAIL: str | None
    AGENCY: int
    CREATE_USER: str
    SUPERVISOR: str | None
    STATUS_USER: str


class ResponseSupervisores(BaseModel):
    ID: int
    NAME: str


class PermissionCreateAndDisableUser(Enum):
    MANAGER = 1
    ADMIN = 2
    DEVELOPER = 3


class ResponseCreateUser(BaseModel):
    SUCCESS: bool
    
