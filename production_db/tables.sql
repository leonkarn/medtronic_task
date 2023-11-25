-- Create Users Table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    join_year INTEGER NOT NULL
);

-- Create Hobbies Table
CREATE TABLE hobbies (
    hobby_id SERIAL PRIMARY KEY,
    hobby_name TEXT NOT NULL
);

-- Create User-Hobbies Relationship Table
CREATE TABLE user_hobbies (
    user_id INTEGER,
    hobby_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (hobby_id) REFERENCES hobbies(hobby_id)
);

-- Insert Users
INSERT INTO users (name, join_year) VALUES ('Hans', 2018);
INSERT INTO users (name, join_year) VALUES ('Klara', 2019);
INSERT INTO users (name, join_year) VALUES ('Sakura', 2020);

-- Insert Hobbies
INSERT INTO hobbies (hobby_name) VALUES ('knitting');
INSERT INTO hobbies (hobby_name) VALUES ('watching tellie');
INSERT INTO hobbies (hobby_name) VALUES ('sky diving');

-- Link Users and Hobbies
-- Ensure that user_id and hobby_id values correspond to existing records in users and hobbies tables
INSERT INTO user_hobbies (user_id, hobby_id) VALUES (1, 1);
INSERT INTO user_hobbies (user_id, hobby_id) VALUES (1, 2);
INSERT INTO user_hobbies (user_id, hobby_id) VALUES (2, 3);
INSERT INTO user_hobbies (user_id, hobby_id) VALUES (3, 2);
INSERT INTO user_hobbies (user_id, hobby_id) VALUES (3, 3);

