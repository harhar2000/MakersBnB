from lib.users import *

class UserRepository:

    def __init__(self, connection):
        self.connection = connection

    
    def all(self):
        rows = self.connection.execute('SELECT * from users')
        users = []
        for row in rows:
            item = User(row["id"], row["user_name"], row["email"], row["user_password"])
            users.append(item)
        return users
    

    def find(self, user_id):
        rows = self.connection.execute(
            'SELECT * from users WHERE id = %s', [user_id])
        row = rows[0]
        return User(row["id"], row["user_name"], row["email"], row["user_password"])
    
    def create(self, user):
        self.connection.execute('INSERT INTO users (user_name, email, user_password) VALUES (%s, %s, %s)', [
                                user.user_name, user.email, user.user_password])
        return None