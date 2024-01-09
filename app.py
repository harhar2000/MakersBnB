import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository
from lib.space import Space

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/index', methods=['GET'])
def get_spaces():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    spaces = repository.all()
    return render_template('spaces/index.html', spaces=spaces)

@app.route('/list_a_space', methods=['GET'])
def get_list_a_space():
    return render_template('spaces/list_a_space.html')

@app.route('/list_a_space', methods=['GET'])
def get_spaces():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    space = Space(None, request.form["space_name"], request.form["space_description"], request.form["price"], request.form["user_id"])
    
    new_space = repository.create(space)
    return redirect('/space_successfully_listed')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 4845)))
