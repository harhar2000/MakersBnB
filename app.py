import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.users_repository import *
from lib.users import *

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('users/index.html')


@app.route("/index/new")
def get_sign_up_page():
    return render_template("users/new.html")


@app.route("/index/about", methods=['GET'])
def get_about():
    return render_template('users/about.html')


@app.route("/index/new", methods=["POST"])
def create_user():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)

    user_name = request.form['user_name']
    email = request.form['email']
    password = request.form['user_password']
    
    user = User(None, user_name, email, password)

    if not user.is_valid():
        errors = user.generate_errors()
        return render_template("users/new.html", errors=errors)

    repository.create(user)

    return redirect('/index')





# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
