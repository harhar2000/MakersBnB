class LoginValidator:

    def __init__(self, email, user_password):
        self.email = email
        self.user_password = user_password

    
    def is_valid(self):
        return self._is_email_valid() and self._is_user_password_valid()
    
    def generate_errors(self):
        errors = []
        if not self._is_email_valid():
            errors.append("Email must not be blank")
        if not self._is_user_password_valid():
            errors.append("Password must not be blank")    
        return errors

    
    def _is_email_valid(self):
        if self.email is None:
            return False
        if self.email == "":
            return False
        return True
    
    def _is_user_password_valid(self):
        if self.user_password is None:
            return False
        if self.user_password == "":
            return False
        return True
    
    # def _is_release_year_valid(self):
    #     if self.release_year is None:
    #         return False
    #     if not self.release_year.isdigit():
    #         return False
    #     return True
    
    def get_valid_email(self):
        if not self._is_email_valid():
            raise ValueError("Cannot get valid email")
        return self.email
    
    def get_valid_user_password(self):
        if not self._is_user_password_valid():
            raise ValueError("Cannot get valid password")
        return self.user_password