-- Create a database assigning a default value to id
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);