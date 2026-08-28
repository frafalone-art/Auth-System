import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from server.database import Base
from server.main import app, get_db, login_attempts


# DB SQLite in memoria, isolato dal vero users.db.
# StaticPool serve perché SQLite in-memory di default crea un DB
# diverso per ogni connessione: con StaticPool ne condividiamo una sola.
TEST_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture()
def client():
    # Tabelle pulite a ogni test
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # Il dizionario dei tentativi di login vive in memoria nel modulo
    # main.py: va svuotato a ogni test, altrimenti il rate limiting
    # di un test "contamina" quello successivo.
    login_attempts.clear()

    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture()
def valid_user():
    return {
        "username": "francesco",
        "email": "francesco@example.com",
        "password": "Password123",
    }
