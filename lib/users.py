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