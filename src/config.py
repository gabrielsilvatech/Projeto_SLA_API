import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    ROUTE_API = os.getenv('ROUTE_API')
    USERNAME = os.getenv('USERNAME_DOCS')
    PASSWORD = os.getenv('PASSWORD_DOCS')
    ROUTE_FRONT = os.getenv('ROUTE_FRONT')

settings = Settings()
