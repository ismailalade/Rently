CREATE DATABASE property_listing;

USE property_listing;


CREATE TABLE landlords (
    landlord_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL
);

CREATE TABLE properties (
    property_id INT AUTO_INCREMENT PRIMARY KEY,
    landlord_id INT,
    property_type VARCHAR(50) NOT NULL,
    location VARCHAR(100) NOT NULL,
    address VARCHAR(200) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (landlord_id) REFERENCES landlords(landlord_id)
);
