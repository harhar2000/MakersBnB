from lib.space import Space


class SpaceRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all spaces
    def all(self):
        rows = self._connection.execute('SELECT * from spaces')
        spaces = []
        for row in rows:
            item = Space(row["id"], row["space_name"], row["space_description"], row["price"], row["host_id"])
            spaces.append(item)
        return spaces
    
    # Create a new space
    def create(self, new_space):
        rows = self._connection.execute('INSERT INTO spaces (space_name, space_description, price, host_id) VALUES (%s, %s, %s, %s) RETURNING id', [
                                    new_space.space_name, new_space.space_description, new_space.price, new_space.host_id])
        row = rows[0]
        new_space.id = row["id"]
        return new_space
        
        
    def find_by_username(self, username):
        rows = self._connection.execute(
            "SELECT users.id AS user_id, users.user_name, spaces.id AS spaces_id, spaces.space_name, spaces.space_description, spaces.price, spaces.host_id AS host_id " \
            "FROM users JOIN spaces ON users.id = spaces.host_id " \
            "WHERE users.user_name = %s", [username])
        space_list = []
        for row in rows:
            item=Space(row["spaces_id"], row["space_name"], row["space_description"], row["price"], row["host_id"])
            space_list.append(item)    
        return space_list

    # def find_by_user(self, user_id):
    #     rows = self._connection.execute(
    #         "SELECT users.id AS user_id, users.email, posts.id AS post_id, posts.message AS message, posts.time AS time, posts.user_id AS user_id, posts.username AS post_username " \
    #         "FROM users JOIN posts ON users.id = posts.user_id " \
    #         "WHERE users.id = %s", [user_id])
    #     posts = []
    #     for row in rows:
    #         post = Post(row["post_id"], row["message"], row["time"], row["user_id"], row["post_username"])
    #         posts.append(post)
    #     posts.reverse()
    #     return posts