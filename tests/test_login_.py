from lib.login import LoginUser
def test_user_can_login():
    user = LoginUser(1, "Test User", "Test Email", "Test Password")
    assert user.id == 1
    assert user.user_name == "Test User"
    assert user.email == "Test Email"
    assert user.user_password == "Test Password"