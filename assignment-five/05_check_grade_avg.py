import pytest
import main

grade_list = [
    100,
    92.45,
    68.18,
    77.77,
    82.35
]

def test_grade_avg_matches():
    grade_avg = main.get_grade_average()
    correct_avg = 0
    grade_avg_matches = False
    """
    This function will be passed an average grade for an assignment
    and make sure it matches the average of the above grades
    """
    print("\nRunning test_grade_avg_matches: ", grade_avg)
    for x in grade_list:
        correct_avg += x
    correct_avg /= len(grade_list)
    assert correct_avg == grade_avg
    

def test_grade_avg_matches_fail():
    grade_avg = main.get_grade_average_fail()
    correct_avg = 0
    grade_avg_matches = False
    """
    This function will be passed an average grade for an assignment
    and make sure it matches the average of the above grades
    """
    print("\nRunning test_grade_avg_matches_fail: ", grade_avg)
    for x in grade_list:
        correct_avg += x
    correct_avg /= len(grade_list)
    assert correct_avg == grade_avg