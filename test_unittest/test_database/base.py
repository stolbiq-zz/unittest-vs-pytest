from unittest import TestCase

from database_classes import Connection, Session


class SetupBaseTestCase(TestCase):
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
