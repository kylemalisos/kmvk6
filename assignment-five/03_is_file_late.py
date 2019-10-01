import pytest
import main
import datetime


def test_is_file_late():
    (submitted_date, due_date, is_late) = main.get_submission_date_info()
    late_correct = False
    """
    If the file is submitted after the due date then is_late should
    be True
    """
    print("\nRunning test_is_file_late: ", submitted_date, due_date, is_late)
    if submitted_date < due_date and is_late == False:
        late_correct = True
    elif submitted_date > due_date and is_late == True:
        late_correct = True
    else:
        late_correct = False
    assert late_correct == True

def test_is_file_late_fail():
    (submitted_date, due_date, is_late) = main.get_submission_date_info_fail()
    late_correct = False
    """
    This test will fail because it is marked as late even though it was
    submitted before the due date
    """
    print("\nRunning test_is_file_late_fail: ", submitted_date, due_date, is_late)
    if submitted_date < due_date and is_late == False:
        late_correct = True
    elif submitted_date > due_date and is_late == True:
        late_correct = True
    else:
        late_correct = False
    assert late_correct == True