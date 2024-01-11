from lib.login import LoginUser
def test_user_can_login():
<<<<<<< HEAD
    user = LoginUser(1, "Test User", "test email", "Test Password")
    assert user.id == 1
    assert user.user_name == "Test User"
    assert user.email == "test email"
=======
    user = LoginUser(1, "Test User", "Test Email", "Test Password")
    assert user.id == 1
    assert user.user_name == "Test User"
    assert user.email == "Test Email"
>>>>>>> 42d467ce751b6b98c1219cb0e7f92109ea9f759d
    assert user.user_password == "Test Password"