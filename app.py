import os
from flask import Flask, request, render_template, redirect, session, Response
from flask_bootstrap import Bootstrap
from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository
from lib.space import Space
from lib.login_repository import LoginRepository
from lib.login import LoginUser
from lib.login_validator import LoginValidator
from lib.users_repository import *
from lib.users import *

import json
import secrets

# Create a new Flask app
app = Flask(__name__)
Bootstrap(app)

"""
Routes for Users
"""
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

    if 'token' in session:
        response = {'token': session['token'], 'message': 'Already logged in'}
        return Response(json.dumps(response), status=200, mimetyoe='application/json')
    
    else:
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

        return redirect('/login')

"""
Routes for login
"""

@app.route('/login',methods=['GET'])
def get_login():
    return render_template('login/login.html')


@app.route("/login", methods=["POST"])
def login_user():
    if 'token' in session:
        response = {'token': session['token'], 'message': 'Already logged in'}
        return Response(json.dumps(response), status=200, mimetyoe='application/json')
    
    else:
        connection = get_flask_database_connection(app)
        repository = LoginRepository(connection)
        validator = LoginValidator(
            request.form['user_name'],
            request.form['user_password']
        )
        if not validator.is_valid():
            errors = validator.generate_errors()
            return render_template("login/login.html", errors=errors)
        
        user_name = request.form['user_name']
        user_password = request.form['user_password']
        result = repository.find(user_name, user_password)
        print("result",result)

        if result:
            token = secrets.token_urlsafe(64)
            session['token'] = token
            print(session['token'])
            login = LoginUser(
                None,
                validator.get_valid_user_name(),
                validator.get_valid_user_password(),
                result.id
            )
            return redirect(f"/spaces")
        else:
            return Response(response={}, status=400, mimetype='application/json')
        
@app.route('/logout',methods=['GET'])
def get_logout():
    session.pop('token', None)
    print("session ended")
    return redirect(f"/index")


"""
Routes for spaces
"""

@app.route('/spaces', methods=['GET'])
def get_spaces():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    spaces = repository.all()
    return render_template('spaces/spaces.html', spaces=spaces)

@app.route('/list_a_space', methods=['GET'])
def get_list_a_space():
    return render_template('spaces/list_a_space.html')

@app.route('/list_a_space', methods=['POST'])
def create_spaces():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    space = Space(None, request.form["space_name"], request.form["space_description"], request.form["price"], 1)
    
    repository.create(space)
    return redirect('/spaces')



@app.route('/requests', methods=['GET'])
def get_requests():
    return render_template('spaces/requests.html')

@app.route('/requests', methods=['POST'])
def get_requests_page():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    user = request.form["user_name"]
    spaces = repository.find_by_username(user)

    return render_template('spaces/requests.html', spaces=spaces)

# start the server and set the secret key and session type
if __name__ == '__main__':
    app.secret_key = b'secretkey'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True, port=int(os.environ.get('PORT', 4845)))