DROP TABLE IF EXISTS tags;

CREATE TABLE tags (
    epc VARCHAR(24) PRIMARY KEY,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT,
    comment TEXT,
    original_register TEXT NOT NULL,
    last_register TEXT
);
