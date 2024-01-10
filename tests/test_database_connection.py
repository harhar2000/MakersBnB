# This is an example of how to use the DatabaseConnection class

"""
When I seed the database
I get some records back
"""
# Testing can connect to database
# def test_database_connection(db_connection):
#     # Seed the database with some test data
#     db_connection.seed("seeds/makersbnb.sql")

#     # Insert a new record
#     #db_connection.execute("INSERT INTO test_table (name) VALUES (%s)", ["second_record"])

#     # Retrieve all records
#     result = db_connection.execute("SELECT * FROM users")

#     # Assert that the results are what we expect
#     assert result == [
#         {"id": 1, "user_name": "test user name","email":"test email","password":"test password"}
#     ]
# def test_database_connection(db_connection):
#     # Seed the database with some test data
#     db_connection.seed("seeds/makersbnb.sql")

#     # Insert a new record
#     db_connection.execute("INSERT INTO users (user_name,user_email,) VALUES (%s)", ["test user name"])

#     # Retrieve all records
#     result = db_connection.execute("SELECT * FROM test_table")

#     # Assert that the results are what we expect
#     assert result == [
#         {"id": 1, "name": "first_record"},
#         {"id": 2, "name": "second"}
#     ]