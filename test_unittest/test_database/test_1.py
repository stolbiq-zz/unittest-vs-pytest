from unittest import TestCase

from database_classes import Session, Connection

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

    def test_data_base_save(self):
        print('######## running save')

    def test_data_base_delete(self):
        print('######## running delete')
