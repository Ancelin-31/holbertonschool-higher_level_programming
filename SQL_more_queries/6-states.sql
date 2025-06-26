-- Creates a database and a first related table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL UNIQUE PRIMARY KEY AUTO-INCREMENT,
    name VARCHAR(256) NOT NULL
);