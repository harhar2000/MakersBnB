from lib.space_repository import SpaceRepository
from lib.space import Space

"""
When we call SpaceRepository#all
We get a list of Space objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    # Seed our database with some test data
    db_connection.seed("seeds/makersbnb.sql")
    repository = SpaceRepository(db_connection) # Create a new SpaceRepository

    spaces = repository.all() # Get all spaces

    # Assert on the results
    assert spaces == [
        Space(1,'test space name', 'test space description', 1, 1),
    ]


"""
When we call SpaceRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    
    db_connection.seed("seeds/makersbnb.sql")
    repository = SpaceRepository(db_connection)

    created_space = repository.create(Space(None, "another_space_name", "another_description", 2, 1))
    assert created_space == Space(2, "another_space_name", "another_description", 2, 1)

    result = repository.all()
    assert result == [
        Space(1,'test space name', 'test space description', 1, 1),
        Space(2, "another_space_name", "another_description", 2, 1)
    ]
    
    db_connection.execute('DELETE FROM spaces WHERE space_name = %s',["another_space_name"])

