import pytest

@pytest.mark.usefixtures('session')
def test_db_save():
    """Test db save"""
    print('######## running save')

def test_db_delete(session):
    """Test db deletion"""
    print('######## running delete')

def test_non_db():
    print('######## non db test')
