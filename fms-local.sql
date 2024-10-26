CREATE DATABASE fms;

USE fms;

CREATE TABLE paddocks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    area FLOAT,
    dm_per_ha FLOAT
);

CREATE TABLE mobs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    paddock_id INT,
    FOREIGN KEY (paddock_id) REFERENCES paddocks(id)
);

CREATE TABLE stock (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mob_id INT,
    age_years INT,
    FOREIGN KEY (mob_id) REFERENCES mobs(id)
);
