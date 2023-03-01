from pydantic import BaseSettings
from fastapi.templating import Jinja2Templates
from pathlib import Path

class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação 
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "mongodb://localhost:27017"

    TEMPLATES = Jinja2Templates(directory='templates')
    MEDIA = Path('media')
    
    JWT_SECRET: str = '9l4k9z6Qgr6-Ar8EfOHPuonKWGMoUR8TfbN1S52irPA'

    ALGORITHM: str = 'HS256'

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True

settings = Settings()