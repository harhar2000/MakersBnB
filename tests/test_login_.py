from lib.login import LoginUser
def test_user_can_login():
    user = LoginUser(1, "Test User", "test email", "Test Password")
    assert user.id == 1
    assert user.user_name == "Test User"
    assert user.email == "test email"
    assert user.user_password == "Test Password"