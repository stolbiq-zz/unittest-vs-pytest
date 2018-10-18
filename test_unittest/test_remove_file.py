from unittest import TestCase
from remove_file import remove_file
from unittest.mock import patch

class BasicTestCase(TestCase):
    @patch('os.remove')
    def test_remove_file_is_called(self, mock_remove):
        remove_file('file')
        mock_remove.assert_called_once_with('file')
