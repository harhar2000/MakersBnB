from lib.login import LoginUser
def test_user_can_login():
    user = LoginUser("Test User", "Test Password")
    assert user.user == "Test User"
    assert user.user_password == "Test Password"