from datetime import date,datetime
from sqlalchemy.orm import class_mapper


class Conversor():

    def __init__(self) -> None:
        pass

    def sqlalchemy_object_to_dict(self,obj:object):
        """Converte uma entidade do SQLAlchemy em um dicionário."""
        columns = [column.key for column in class_mapper(obj.__class__).columns]
        result_dict = {column: getattr(obj, column) for column in columns}

        # Trata objetos 'date' convertendo-os para strings no formato ISO
        for key, value in result_dict.items():
            if isinstance(value, date):
                result_dict[key] = value.isoformat()

        # Aplica strip() em strings
        for key, value in result_dict.items():
            if isinstance(value, str):
                result_dict[key] = value.strip()

        return result_dict
    
    def converter_para_datetime(self, data_str: str) -> date:
        return datetime.strptime(data_str, "%d/%m/%Y")