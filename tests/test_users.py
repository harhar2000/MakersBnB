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


"""
We can assess a book for validity
"""
def test_user_validity():
    assert User(1, "", "", "").is_valid() == False
    assert User(1, "Username", "", "").is_valid() == False
    assert User(1, "", "Email", "").is_valid() == False
    assert User(1, "User name", None, None).is_valid() == False
    assert User(1, None, "Author", None).is_valid() == False
    assert User(1, "User name", "User email", "User password").is_valid() == True
    assert User(None, "User name", "User email", "User password").is_valid() == True



"""
We can generate errors for an invalid user
"""
def test_user_errors():
    assert User(1, "", "", "").generate_errors() == "User name can't be blank, User email can't be blank, User password can't be blank"
    assert User(1, "Title", "", "").generate_errors() == "User email can't be blank, User password can't be blank"
    assert User(1, "", "Author", "").generate_errors() == "User name can't be blank, User password can't be blank"
    assert User(1, "Title", None, None).generate_errors() == "User email can't be blank, User password can't be blank"
    assert User(1, None, "Author", None).generate_errors() == "User name can't be blank, User password can't be blank"
    assert User(1, "User name", "User email", "User password").generate_errors() == None
    assert User(None, "User name", "User email", "User password").generate_errors() == None