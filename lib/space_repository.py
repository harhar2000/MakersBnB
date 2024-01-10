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
            item = Space(row["id"], row["space_name"], row["space_description"], row["price"], row["user_id"])
            spaces.append(item)
        return spaces
    
    # Create a new space
    def create(self, new_space):
        rows = self._connection.execute('INSERT INTO spaces (space_name, space_description, price, user_id) VALUES (%s, %s, %s, %s) RETURNING id', [
                                    new_space.space_name, new_space.space_description, new_space.price, new_space.user_id])
        row = rows[0]
        new_space.id = row["id"]
        return new_space
