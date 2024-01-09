-- Drop the 'users' table if it exists, along with any dependent objects
DROP TABLE IF EXISTS users CASCADE;

-- Create the 'users' table
CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    user_name TEXT,
    email TEXT,
    user_password TEXT
);

-- Drop the 'spaces' table if it exists, along with any dependent objects
DROP SEQUENCE IF EXISTS spaces;
DROP TABLE IF EXISTS spaces;

-- Create the 'spaces' table
CREATE TABLE spaces(
    id SERIAL PRIMARY KEY,
    space_name TEXT,
    space_description TEXT,
    price INT,
    user_id INT,
    CONSTRAINT fk_users FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Insert a test record into the 'users' table
INSERT INTO users (user_name, email, user_password) VALUES ('test user name', 'test email', 'test password');

-- Insert a test record into the 'spaces' table
INSERT INTO spaces (space_name, space_description, price, user_id) VALUES ('test space name', 'test space description', 1, 1);