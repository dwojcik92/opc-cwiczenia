-- CREATE DATABASE IF NOT EXISTS train_database;

-- USE train_database;

-- CREATE TABLE IF NOT EXISTS trains (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     name VARCHAR(255) NOT NULL
-- );

-- INSERT INTO trains (name) VALUES ('Example Data 1'), ('Example Data 2'), ('Example Data 3');


-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS train_database;

-- Use the created database
USE train_database;

-- Create table for trains
CREATE TABLE IF NOT EXISTS trains (
    train_id INT AUTO_INCREMENT PRIMARY KEY,
    train_name VARCHAR(255) NOT NULL,
    departure_time INT NOT NULL,
    arrival_time INT NOT NULL,
    departure_station VARCHAR(100) NOT NULL,
    arrival_station VARCHAR(100) NOT NULL
);

-- Generate and insert sample train data
INSERT INTO trains (train_name, departure_time, arrival_time, departure_station, arrival_station)
SELECT
    CONCAT('Train ', numbers.n) AS train_name,
    FLOOR(RAND() * 86400) AS departure_time,
    FLOOR(RAND() * 86400) AS arrival_time,
    CONCAT('Station ', FLOOR(RAND() * 1000)) AS departure_station,
    CONCAT('Station ', FLOOR(RAND() * 1000)) AS arrival_station
FROM (
    SELECT 
        (a.n + b.n * 10 + c.n * 100) AS n
    FROM
        (SELECT 0 AS n UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9) AS a,
        (SELECT 0 AS n UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9) AS b,
        (SELECT 0 AS n UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9) AS c
) AS numbers
LIMIT 1000;
