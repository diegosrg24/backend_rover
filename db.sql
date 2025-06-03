CREATE DATABASE esp32_data;

USE esp32_data;

CREATE TABLE readings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    value FLOAT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
    