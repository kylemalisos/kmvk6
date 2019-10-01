import pytest
import main

pawprint_clearence = [
    ("SGVG6", "admin"),
    ("CHYH2", "ta"),
    ("KMVK6", "user"),
    ("JALA9", "user")
]

def test_pawprint_matches_clearence():
    (pawprint, clearence) = main.get_pawprint_clearence()
    clearence_matches = False
    """
    This function will be passed a pawprint and a clearence level
    if the clearence matches the info above it will pass
    """
    print("\nRunning test_pawprint_matches_clearence: ", pawprint, clearence)
    for (x,y) in pawprint_clearence:
        if x == pawprint and y == clearence:
            clearence_matches = True
    assert clearence_matches == True

def test_pawprint_matches_clearence_fail():
    (pawprint, clearence) = main.get_pawprint_clearence_fail()
    clearence_matches = False
    """
    This function will be passed a pawprint and a clearence level
    if the clearence matches the info above it will pass
    """
    print("\nRunning test_pawprint_matches_clearence_fail: ", pawprint, clearence)
    for (x,y) in pawprint_clearence:
        if x == pawprint and y == clearence:
            clearence_matches = True
    assert clearence_matches == True