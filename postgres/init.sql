-- Create the users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
-- Insert initial data into users table
INSERT INTO users (username, email) VALUES
('user 01', 'user01@example.com'),
('user 02', 'user02@example.com');