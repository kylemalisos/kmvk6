import pytest
import main


def test_correct_file_type():
    name = main.get_filename()
    """
    This test will make sure that the file type is in a ".zip" format
    """
    print("\nRunning test_correct_file_type: ", name)
    assert name.endswith('.zip')

def test_correct_file_type_fail():
    name = main.get_filename_fail()
    """
    This test will fail because the file ends with ".pdf" instead of ".zip"
    """
    print("\nRunning test_correct_file_type_fail: ", name)
    assert name.endswith('.zip')