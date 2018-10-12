import pytest

from setup_classes import Session, Connection


@pytest.fixture
def session():
    session = Session()
    yield session
    session.close()

@pytest.fixture(scope='module', autouse=True)
def connection():
    connection = Connection()
    yield connection
    connection.close()
