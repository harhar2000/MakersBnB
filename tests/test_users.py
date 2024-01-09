from lib.users import *

"""
Testing the creation of user details
"""

def test_user_detail_creation():
    user = User(1, "Test user name", "Test email", "Test user_password")
    assert user.user_name == "Test user name"
    assert user.email == "Test email"
    assert user.user_password == "Test user_password"


"""
We can format users to strings nicely
"""
def test_users_format_nicely():
    user = User(1, "Test user name", "Test email", "Test user_password")
    assert str(user) == "User(1, Test user name, Test email, Test user_password)"
    

"""
We can compare two identical artists
And have them be equal
"""
def test_users_are_equal():
    user1 = User(1, "Test user name", "Test email", "Test user_password")
    user2 = User(1, "Test user name", "Test email", "Test user_password")
    assert user1 == user2