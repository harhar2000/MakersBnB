from lib.users import *
from lib.users_repository import *

"""
When we call UserRepository #all
We get a list of User objects reflecting the seed data.
"""
def test_get_all_users(db_connection): 
    db_connection.seed("seeds/makersbnb.sql") 
    repository = UserRepository(db_connection) 

    users = repository.all() 

    assert users == [
        User(1, "test user name", "test email", "test password")
    ]


"""
When we call UserRepository#find
We get a single User object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)

    user = repository.find(1)
    assert user == User(1, "test user name", "test email", "test password")



"""
When we call UsersRepository#create
We get a new user in the database.
"""
def test_create_user(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)

    repository.create(User(None, "Harry123", "Harry email", "Harry password"))

    result = repository.all()
    assert result == [
        User(1, "test user name", "test email", "test password"),
        User(2, "Harry123", "Harry email", "Harry password")
    ]
