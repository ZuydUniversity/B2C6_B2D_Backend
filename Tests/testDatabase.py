from fastapi.testclient import TestClient
from App.Data.Database import get_db
from App.Data.DatabaseModels import Base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import pytest

from main import app

SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://root:Welkom123!@localhost:3306/jdb_db_test"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


@pytest.fixture
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)