from pydantic import BaseModel

class BaseCarteira(BaseModel):
    ID_AGENCY : int
    NAME_AGENCY : str