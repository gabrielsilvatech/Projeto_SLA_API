from sqlalchemy import Column, VARCHAR, Integer,BOOLEAN
from sqlalchemy.orm import  declarative_base
from typing import cast

from src.model.user.user_type import UserType
from src.model.user.user_status import UserStatus
from src.model.agency.agency_type import AgencyType
from src.model.user.user_role import UserRole

Base = declarative_base()

class User(Base):
    
    __tablename__ = "tb_users"

    _id = Column("id", VARCHAR(255), primary_key=True, nullable=False)
    _name = Column("name", VARCHAR(200), nullable=False)
    _cpf = Column("cpf", VARCHAR(11),nullable=False,unique=True)
    _role = Column("role", Integer, nullable=False)
    _agency = Column("agency", Integer, nullable=False)
    _type = Column("type", Integer, nullable=False)
    _contract = Column("contract", Integer, nullable=False)
    _status_user = Column("status_user", Integer, nullable=False)
    _login = Column("login", VARCHAR(50), nullable=False,unique=True)
    _password = Column("password", VARCHAR(60), nullable=False)
    _email = Column("email", VARCHAR(255), nullable=False)
    _id_supervisor = Column("id_supervisor", VARCHAR, nullable=True)
    _id_creator_user = Column("id_creator_user", VARCHAR, nullable=False)
    _password_reset = Column("password_reset",BOOLEAN,nullable=False)
    
    
    @property
    def id(self) -> str:
        return cast(str, self._id)

    @property
    def name(self) -> str:
        return cast(str, self._name)
    
    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def cpf(self) -> str:
        return cast(str, self._cpf)
    
    @cpf.setter
    def cpf(self, value: str) -> None:
        self._cpf = value

    @property
    def role(self) -> int:
        return cast(int, self._role)
    
    @role.setter
    def role(self, value: UserRole) -> None:
        self._role = value.value

    @property
    def agency(self) -> int:
        return cast(int, self._agency)
    
    @agency.setter
    def agency(self, value: AgencyType) -> None:
        self._agency = value.value

    @property
    def type(self) -> UserType:
        return UserType(self._type)

    @type.setter
    def type(self, value: UserType) -> None:
        self._type = value.value
        
    @property
    def contract(self) -> int:
        return cast(int, self._contract)

    @contract.setter
    def contract(self, value: int) -> None:
        self._contract = value

    @property
    def status_user(self) -> UserStatus:
        return UserStatus(self._status_user)
    
    @status_user.setter
    def status_user(self, value: UserStatus) -> None:
        self._status_user = value.value

    @property
    def login(self) -> str:
        return cast(str, self._login)
    
    @login.setter
    def login(self, value: str) -> None:
        self._login = value

    @property
    def password(self) -> str:
        return cast(str, self._password)
    
    @password.setter
    def password(self, value: str) -> None:
        self._password = value

    @property
    def email(self) -> str:
        return cast(str, self._email)
    
    @email.setter
    def email(self, value: str) -> None:
        self._email = value

    @property
    def id_supervisor(self) -> str:
        return cast(str, self._id_supervisor)
    
    @id_supervisor.setter
    def id_supervisor(self, value: str) -> None:
        self._id_supervisor = value

    @property
    def id_creator_user(self) -> str:
        return cast(str, self._id_creator_user)
    
    @id_creator_user.setter
    def id_creator_user(self, value: str) -> None:
        self._id_creator_user = value
    
    @property
    def password_reset(self) -> bool:
        return cast(bool,self._password_reset)

    @password_reset.setter
    def password_reset(self, value: bool) -> None:
        self._password_reset = value