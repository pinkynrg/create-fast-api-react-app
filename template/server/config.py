from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    postgres_user: str = "root"
    postgres_password: str = "root"
    postgres_host: str = "127.0.0.1"
    postgres_db: str = "db"

    @property
    def database_url(self) -> str:
        return f"postgresql://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}/{self.postgres_db}"

    class Config:
        env_file = ".env"

settings = Settings()