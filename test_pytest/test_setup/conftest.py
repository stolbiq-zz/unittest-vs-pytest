import pytest

from setup_classes import Session


@pytest.fixture
def session():
    session = Session()
    yield session
    session.close()
