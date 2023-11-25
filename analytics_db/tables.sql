-- Create Users Table
CREATE TABLE hobbies_analysis (
    id SERIAL PRIMARY KEY,
    hobby_name VARCHAR(255) NOT NULL,
    join_year INTEGER NOT NULL
);
