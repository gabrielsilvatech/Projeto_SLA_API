from geopy.geocoders import Nominatim#type:ignore



class Ibge():


    def __init__(self) -> None:
        self.geolocator = Nominatim(user_agent="my_app")

        self.estados_brasileiros = [
            "Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Distrito Federal", 
            "Espírito Santo", "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul", 
            "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro", 
            "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia", "Roraima", "Santa Catarina", 
            "São Paulo", "Sergipe", "Tocantins"
        ]


    def identificador_estado(self,cidade:str) -> str | bool:

        location = self.geolocator.geocode(cidade + ", Brazil", addressdetails=True)#type:ignore
        if location:

            partes_endereco = location.address.split(", ")#type:ignore
            
            for parte in partes_endereco:#type:ignore
                if parte in self.estados_brasileiros:
                    estado = parte#type:ignore
                    break
            if estado:#type:ignore
                return str(estado).upper()#type:ignore
            else:
                return False
        else:
            return False