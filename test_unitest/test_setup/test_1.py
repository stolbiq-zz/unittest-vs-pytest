from unittest import TestCase

from setup_classes import Session, Connection

class Setup1TestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.connection = Connection()

    @classmethod
    def tearDownClass(cls):
        cls.connection.close()

    def setUp(self):
        self.session = Session()

    def tearDown(self):
        self.session.close()

    def test_db_save(self):
        """Test db save"""
        print('######## running save')

    def test_db_delete(self):
        """Test db deletion"""
        print('######## running delete')
