from unittest import TestCase

from setup_classes import Session

class Setup1TestCase(TestCase):

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
