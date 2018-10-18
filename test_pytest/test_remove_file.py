from remove_file import remove_file

def test_remove_file_is_called(mocker):
    mock_remove = mocker.patch('os.remove')
    remove_file('file')
    mock_remove.assert_called_once_with('file')
