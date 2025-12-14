CREATE DATABASE mydatabase;

USE mydatabase;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    age INT
);

INSERT INTO users (name, email, age) VALUES
('Alice', 'alice@gmail.com', 25),
('Bob', 'bob@gmail.com', 30),
('Charlie', 'charlie@gmail.com', 28);

SELECT * FROM users;
