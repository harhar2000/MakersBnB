from lib.login import LoginUser

class LoginRepository():
    def __init__(self,connection):
        self.connection = connection


    def find(self, id, user_password):
        rows = self.connection.execute('SELECT * FROM users WHERE user_name = %s AND user_password = %s',[id,user_password])
        if len(rows) == 0:
            return None
        else:
            row = rows[0]
            return LoginUser(row["id"],row["user_name"],row["email"],row["user_password"])