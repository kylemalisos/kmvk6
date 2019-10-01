import pytest
import datetime

#For test one
def get_filename():
    """
    This function will return a string which would be a student
    submitted file name
    """
    print("\n(Returning string from get_filename)")
    return "studentSubmission.zip"

def get_filename_fail():
    """
    This function will return a file name string that is in the
    wrong format
    """
    print("\n(Returning string from get_filename_fail)")
    return "studentSubmission.pdf"

#For test two
def get_login_info():
    """
    This function returns a username and password
    """
    user = ('kyle', 'password1234')
    print("\n(Returning tuple from get_login_info)")
    return user

def get_login_info_fail():
    """
    This function returns a username and password
    """
    user = ('badguy', '187(!&626$*&62698e')
    print("\n(Returning tuple from get_login_info_fail)")
    return user

#For test three
def get_submission_date_info():
    """
    This function is going to return a users submission date,
    due date and if it was marked late
    """
    sub_date = datetime.datetime(2019, 9, 30) 
    due_date = datetime.datetime(2019, 9, 25) 
    info = (sub_date, due_date, True)
    return info

def get_submission_date_info_fail():
    """
    This function is going to return a users submission date,
    due date and an incorrectly marked late = true
    """
    sub_date = datetime.datetime(2019, 9, 22) 
    due_date = datetime.datetime(2019, 9, 25) 
    info = (sub_date, due_date, True)
    return info

#For test four
def get_pawprint_clearence():
    """
    This function will return a pawprint with the correct
    associated clearence level for that pawprint
    """
    clearence = ('SGVG6', 'admin')
    return clearence

def get_pawprint_clearence_fail():
    """
    This function will return a pawprint with the wrong
    associated clearence level for that pawprint
    """
    clearence = ('JALA9', 'ta')
    return clearence

#For test five
def get_grade_average():
    """
    This function will return the average grade on an assignment
    for all students who turned it in
    """
    grade_avg = 84.15
    return grade_avg

def get_grade_average_fail():
    """
    This function will return the average grade on an assignment
    for all students who turned it in but it is incorrect
    """
    grade_avg = 76.54
    return grade_avg