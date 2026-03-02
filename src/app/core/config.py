"""
    Configuration settings for the API application.
"""

from pydantic import BaseSettings

# pylint: disable=too-few-public-methods
class Settings(BaseSettings):
    """
    Settings class for managing application configuration.
    
    Loads configuration from environment variables or .env file.
    Provides access to all application settings needed for API operation.
    """
    app_name: str = "Tienda Plus API"
    debug: bool = True
    secret_key: str = "BAMBY_04"
    access_token_expire_minutes: int = 15
    algorithm: str = "HS256"
    messeng_key: str = "D159S"
    user_bd: str = 'root'
    password_bd: str = '1234'
    host_bd: str = 'mysql'
    port_bd: str = '3306'

    class Config:
        """
        Configuration settings for loading environment variables.
        """
        env_file = ".env"
