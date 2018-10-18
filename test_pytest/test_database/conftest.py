import pytest

from database_classes import Session


@pytest.fixture
def session():
    session = Session()
    yield session
    session.close()
