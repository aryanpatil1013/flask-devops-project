CREATE DATABASE IF NOT EXISTS flaskdb;

USE flaskdb;

CREATE TABLE IF NOT EXISTS names (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

INSERT INTO names (name) VALUES ('Aryan Patil');
INSERT INTO names (name) VALUES ('DevOps Engineer');

