CREATE TABLE users (
    		user_id SERIAL PRIMARY KEY,
    		name VARCHAR(100) NOT NULL,
    		email VARCHAR(100) NOT NULL
);

INSERT INTO users (name, email) 
VALUES
    		('User1', 'user1@mail.com'),
    		('User2', 'user2@mail.com'),
    		('User3', 'user3@mail.com');
