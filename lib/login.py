class LoginUser:
    def __init__(self,user,user_password):
        self.id = id
        self.user = user
        self.user_password = user_password 
    
    def __eq__(self,other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"{self.id},{self.user},{self.user_password}"