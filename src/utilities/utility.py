import bcrypt
from typing import Literal, Any
from fastapi import HTTPException
from validate_docbr import CPF, CNPJ # type: ignore


class Utility:
    
    @staticmethod 
    def validation_doc(doc: str) -> Literal["CPF","CNPJ"]:
        cpf_validator = CPF()
        cnpj_validator = CNPJ()
        doc = doc.strip()
        
        if len(doc) == 11:        
            if cpf_validator.validate(doc):
                return "CPF"
            else:
                raise HTTPException(status_code=409, detail="Documento: UNDEFINED")
        
        elif len(doc) == 14:
            if cnpj_validator.validate(doc):
                return "CNPJ"
            else:
                raise HTTPException(status_code=409, detail="Documento: UNDEFINED")
            
        else:
            raise HTTPException(status_code=409, detail="Documento: UNDEFINED")

    @staticmethod
    def create_hash_password(senha:str):
        salt = bcrypt.gensalt()
        hash_senha = bcrypt.hashpw(senha.encode('utf-8'), salt)
        return hash_senha
    
    @staticmethod
    def update_attribute(old_value: Any, new_value: Any):
        if new_value is not None:
            return new_value
        
        return old_value
