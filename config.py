from typing import Optional
from dataclasses import dataclass, field
from sqlalchemy.engine import URL
from dotenv import load_dotenv
import os


load_dotenv()


@dataclass
class AirConfig:
    name: str = os.getenv("AIR_DB", "name")
    user: str = os.getenv("POSTGRES_USER", "user")
    password: str = os.getenv("POSTGRES_PASSWORD", "password")
    host: str = os.getenv("POSTGRES_HOST", "localhost")
    port: int = os.getenv("POSTGRES_PORT", "5432")

    driver: str = 'psycopg2'
    database_system: str = 'postgresql'

    def build_connection_str(self) -> str:
        """This function build a connection string."""

        return URL.create(
            drivername=f'{self.database_system}+{self.driver}',
            username=self.user,
            database=self.name,
            password=self.password,
            port=self.port,
            host=self.host,
        ).render_as_string(hide_password=False)


@dataclass
class WBConfig:
    name: str = os.getenv("WB_DB", "name")
    user: str = os.getenv("POSTGRES_USER", "user")
    password: str = os.getenv("POSTGRES_PASSWORD", "password")
    host: str = os.getenv("POSTGRES_HOST", "localhost")
    port: int = os.getenv("POSTGRES_PORT", "5432")

    driver: str = 'psycopg2'
    database_system: str = 'postgresql'

    def build_connection_str(self) -> str:
        """This function build a connection string."""

        return URL.create(
            drivername=f'{self.database_system}+{self.driver}',
            username=self.user,
            database=self.name,
            password=self.password,
            port=self.port,
            host=self.host,
        ).render_as_string(hide_password=False)

@dataclass
class CarsConfig:

    name: Optional[str] = os.getenv("CAR_DB", "name")
    user: str = os.getenv("POSTGRES_USER", "user")
    password: str = os.getenv("POSTGRES_PASSWORD", "password")
    host: str = os.getenv("POSTGRES_HOST", "localhost")
    port: int = os.getenv("POSTGRES_PORT", "5432")

    driver: str = 'psycopg2'
    database_system: str = 'postgresql'

    def build_connection_str(self) -> str:
        """This function build a connection string."""

        return URL.create(
            drivername=f'{self.database_system}+{self.driver}',
            username=self.user,
            database=self.name,
            password=self.password,
            port=self.port,
            host=self.host,
        ).render_as_string(hide_password=False)

@dataclass
class Config:
    air: AirConfig = field(default_factory=AirConfig)
    wb: WBConfig = field(default_factory=WBConfig)
    cars: CarsConfig = field(default_factory=CarsConfig)

configuration = Config()
