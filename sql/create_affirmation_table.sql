DROP TABLE IF EXISTS meals;
CREATE TABLE affirmations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    affirmation TEXT NOT NULL UNIQUE,
    deleted BOOLEAN DEFAULT FALSE
);