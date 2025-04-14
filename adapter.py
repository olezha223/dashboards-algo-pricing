from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine, Engine, orm
from sqlalchemy.orm import Session, sessionmaker

from config import configuration


engine_cars: Engine = create_engine(
    url=configuration.cars.build_connection_str(),
    echo=0,
    pool_pre_ping=True
)


SessionLocal_cars = sessionmaker(
    bind=engine_cars,
    expire_on_commit=False,
    class_=Session
)

engine_air: Engine = create_engine(
    url=configuration.cars.build_connection_str(),
    echo=0,
    pool_pre_ping=True
)


SessionLocal_air = sessionmaker(
    bind=engine_air,
    expire_on_commit=False,
    class_=Session
)

engine_wb: Engine = create_engine(
    url=configuration.cars.build_connection_str(),
    echo=0,
    pool_pre_ping=True
)


SessionLocal_wb = sessionmaker(
    bind=engine_wb,
    expire_on_commit=False,
    class_=Session
)



@contextmanager
def get_session_cars() -> Generator[Session, None, None]:
    """
    Context manager для получения сессии SQLAlchemy.
    Обеспечивает транзакционность операций и автоматическое закрытие сессии.
    """
    session = SessionLocal_cars()
    try:
        # Выполняю транзакцию
        yield session
        session.commit()

    except Exception:
        # В случае ошибки откатываю все назад
        session.rollback()
        raise

    finally:
        # В любом случае закрываю соединение
        session.close()


@contextmanager
def get_session_air() -> Generator[Session, None, None]:
    """
        Context manager для получения сессии SQLAlchemy.
        Обеспечивает транзакционность операций и автоматическое закрытие сессии.
        """
    session = SessionLocal_air()
    try:
        # Выполняю транзакцию
        yield session
        session.commit()

    except Exception:
        # В случае ошибки откатываю все назад
        session.rollback()
        raise

    finally:
        # В любом случае закрываю соединение
        session.close()

@contextmanager
def get_session_wb() -> Generator[Session, None, None]:
    """
        Context manager для получения сессии SQLAlchemy.
        Обеспечивает транзакционность операций и автоматическое закрытие сессии.
        """
    session = SessionLocal_wb()
    try:
        # Выполняю транзакцию
        yield session
        session.commit()

    except Exception:
        # В случае ошибки откатываю все назад
        session.rollback()
        raise

    finally:
        # В любом случае закрываю соединение
        session.close()