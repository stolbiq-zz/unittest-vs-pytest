import pytest
from setup_classes import Session

@pytest.fixture
def session():
    Session()

def test_db_save(self):
    """Test db save"""
    print('######## running save')

def test_db_delete(self):
    """Test db deletion"""
    print('######## running delete')

def test_non_db(self):
    print('######## non db test')
