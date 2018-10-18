from unittest import TestCase

from database_classes import Session

class Setup1TestCase(TestCase):

    def setUp(self):
        self.session = Session()

    def tearDown(self):
        self.session.close()

    def test_data_base_save(self):
        print('######## running save')

    def test_data_base_delete(self):
        print('######## running delete')
