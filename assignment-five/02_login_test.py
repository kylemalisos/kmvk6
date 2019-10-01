import pytest
import main

registered_users = [
    ("sean", "augur4life"),
    ("caleb", "plzgivegoodgrade"),
    ("kyle", "password1234"),
    ("jake", "iclimbrocks")
]

def test_login():
    (key, value) = main.get_login_info()
    print(key, value)
    in_list = False
    """
    This test will make sure that the user info is in the registered
    user list
    """
    print("\nRunning test_login: ", key, value)
    for (x,y) in registered_users:
        if x == key and y == value:
            in_list = True
    assert in_list == True

def test_login_fail():
    (key, value) = main.get_login_info_fail()
    in_list = False
    """
    This test will fail because it is not in the registered user list
    """
    print("\nRunning test_login_fail: ", key, value)
    for (x,y) in registered_users:
        if x == key and y == value:
            in_list = True
            print(x,y,key,value)
    assert in_list == True