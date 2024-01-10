from lib.login import LoginUser

class LoginRepository():
    def __init__(self,connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM users')
        user_list = []
        for row in rows:
            user = user_list(row["id"],row["user_name"],row["user_password"])
            user_list.append(user)
        return user_list

    def find(self,id):
        rows = self.connection.execute('SELECT * FROM users WHERE id = %s',[id])
        row = rows[0]
        return LoginUser(row["user_name"],row["user_password"])

    def create(self,id):
        rows = self.connection.execute('SELECT * FROM users WHERE id = %s',[id])
        row = rows[0]
        return LoginUser(row["id"],row["user_name"],row["email"],row['user_password'])