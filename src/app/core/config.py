from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Tienda Plus API"
    DEBUG: bool = True
    SECRET_KEY: str = "BAMBY_04"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    ALGORITHM: str = "HS256"
    MESSENG_KEY: str = "D159S"
    USER_BD: str = 'root'
    PASSWORD_BD: str = '1234'
    HOST_BD: str = 'mysql'
    PORT_BD: str = '3306'

    class Config:
        env_file = ".env"

settings = Settings()