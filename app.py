import os
from flask import Flask, request,redirect, render_template
from lib.database_connection import get_flask_database_connection
from lib.login_repository import LoginRepository
from lib.login import LoginUser

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
# @app.route('/index', methods=['GET'])
# def get_index():
    # return render_template('index.html')

# @app.route('/login', methods=['GET', 'POST'])
# def post_login():
#     if request.method == 'POST':
#         connection = get_flask_database_connection(app)
#         repository = LoginRepository(connection)  # check the Class name
#         login = LoginUser(None, request.form['user_name'], request.form['user_password'])
#         repository.create(login)  # check the Class Name and names
#     return render_template('login.html')


@app.route('/login',methods=['GET'])
def get_login():
    return render_template('login.html')


@app.route("/login", methods=["POST"])
def login_user():
    connection = get_flask_database_connection(app)
    repository = LoginRepository(connection)
    # validator = LoginValidator(
    #     request.form['email'],
    #     request.form['user_password']
    # )
    # if not validator.is_valid():
    #     errors = validator.generate_errors()
    #     return render_template("/login.html", errors=errors)
    # login = Login(
    #     None,
    #     validator.get_valid_email(),
    #     validator.get_valid_user_password(),
    #     1
    # )

    id = ""
    email = ""
    user_name = request.form['user_name']
    user_password = request.form['user_password']
    result = repository.find(user_name, user_password)
    if result is not None:
        return redirect(f"/welcome") #change to space list
    else:
        return redirect(f"/login") #change to sing up page (return)






# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
