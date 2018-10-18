from unittest import TestCase
import pytest

from test_unittest.test_database.base import SetupBaseTestCase

class Setup1TestCase(SetupBaseTestCase):

    def test_data_base_save(self):
        print('######## running save')

    def test_data_base_delete(self):
        print('######## running delete')

    def test_non_data_base(self):
        print('######## running non database test')
