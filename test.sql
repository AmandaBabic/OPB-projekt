CREATE TABLE test (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO test (name, email)
VALUES
('test1', 'test1@email.com'),
('test2', 'test2@email.com');