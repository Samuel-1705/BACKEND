CREATE DATABASE IF NOT EXISTS Team;

USE Team;

CREATE TABLE users(
	user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    profile_image VARCHAR(255)
);

CREATE TABLE servers(
	server_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    icon VARCHAR(255)
);

CREATE TABLE channels(
	channel_id INT AUTO_INCREMENT PRIMARY KEY,
    server_id INT NOT NULL,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    constraint fk_channel_server FOREIGN KEY (server_id) REFERENCES servers(server_id) ON DELETE CASCADE
);

CREATE TABLE messages (
	message_id INT AUTO_INCREMENT PRIMARY KEY,
	user_id INT NOT NULL,
	channel_id INT NOT NULL,
	content TEXT NOT NULL,
	creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	constraint fk_messages_user FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
	constraint fk_messages_channel FOREIGN KEY (channel_id) REFERENCES channels(channel_id) ON DELETE CASCADE
);

CREATE TABLE server_onboarding(
	id INT AUTO_INCREMENT PRIMARY KEY,
	user_id INT NOT NULL,
    server_id INT NOT NULL,
    constraint fk_server_onboarding_user FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
	constraint fk_server_onboarding_server FOREIGN KEY (server_id) REFERENCES servers(server_id) ON DELETE CASCADE
);