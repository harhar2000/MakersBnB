# MakersBnB

## Overview
MakersBnB is a sophisticated Airbnb-like website that caters to users looking to book high-class spaces (venues) for stays. It enables hosts to list their spaces and track bookings, and allows guests to view available dates and secure accommodations.

## Project Structure

### Lib
This directory contains the core functionality of MakersBnB.

- `database_connection.py`: Handles the connection to the database.
- `login_repository.py`: Manages login-related data interactions.
- `login.py`: Facilitates user logins.
- `space_repository.py`: Handles data related to space listings.
- `space.py`: Defines the space entity.
- `users_repository.py`: Manages user data interactions.
- `users.py`: Defines the user entity.

### Seeds
Contains SQL files for database setup.

- `database_connection.sql`: Script for initial database connection setup.
- `makersbnb.sql`: Contains the SQL commands to set up the MakersBnB database schema.

### Static
Holds static files such as stylesheets.

- `style.css`: The main CSS file for styling the website.

### Templates
Organised into subdirectories, these HTML templates define the structure of the web pages.

#### Login
- `login.html`: The login page template.

#### Spaces
- `list_a_space.html`: Template for hosts to list new spaces.
- `requests.html`: Shows booking requests for hosts.
- `spaces.html`: Displays available spaces for booking.

#### Users
- `about.html`: Provides information about MakersBnB.
- `index.html`: The homepage template.
- `new.html`: Used for creating new user accounts.

### Additional Components
- `test/`: Contains tests for the application.
- `app.py`: The main application file for MakersBnB.
- `seed_dev_database.py`: Script to seed the development database.

## Getting Started

To run MakersBnB locally:

1. Clone the repository.
2. Set up the database using the SQL files in the `seeds` directory.
3. Install required dependencies (if any).
4. Run `app.py` to start the application.


# MakersBnB Python Project Seed

This repo contains the seed codebase for the MakersBnB project in Python (using 
Flask and Pytest).

Someone in your team should fork this seed repo to their Github account. 
Everyone in the team should then clone this fork to their local machine to work on it.

## Setup

```shell
# Install dependencies and set up the virtual environment
; pipenv install

# Activate the virtual environment
; pipenv shell

# Install the virtual browser we will use for testing
; playwright install
# If you have problems with the above, contact your coach

# Create a test and development database
; createdb YOUR_PROJECT_NAME
; createdb YOUR_PROJECT_NAME_TEST

# Open lib/database_connection.py and change the database names
; open lib/database_connection.py

# Run the tests (with extra logging)
; pytest -sv

# Run the app
; python app.py

# Now visit http://localhost:5000/index in your browser
```
