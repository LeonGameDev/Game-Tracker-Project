CREATE DATABASE IF NOT EXISTS game_tracker_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE game_tracker_db;

CREATE TABLE IF NOT EXISTS games (
    id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    genre VARCHAR(50) NOT NULL,
    rating INT NOT NULL,
    PRIMARY KEY (id)
);
