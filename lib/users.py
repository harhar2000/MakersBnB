class User:

    def __init__(self, user_id, user_name, email, user_password):
        self.user_id = user_id
        self.user_name = user_name
        self.email = email
        self.user_password = user_password


    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"User({self.user_id}, {self.user_name}, {self.email}, {self.user_password})"
    

    def is_valid(self):
        if self.user_name == None or self.user_name == "":
            return False
        if self.email == None or self.email == "":
            return False
        if self.user_password == None or self.user_password == "":
            return False
        return True



    def generate_errors(self):
        errors = []
        if self.user_name == None or self.user_name == "":
            errors.append("User name can't be blank")
        if self.email == None or self.email == "":
            errors.append("User email can't be blank")
        if self.user_password == None or self.user_password == "":
            errors.append("User password can't be blank")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)