PRAGMA encoding='UTF-8';

CREATE TABLE IF NOT EXISTS election(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS candidate (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS result(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    election_candidate_id INTEGER REFERENCES candidate_in_election(id),
    vote_count INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS fingerprint(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    election_id INTEGER REFERENCES election(id),
    fingerprint TEXT NOT NULL,
    vote_token TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS signature(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vote_token TEXT NOT NULL UNIQUE,
    is_signed INT NOT NULL
);

CREATE TABLE IF NOT EXISTS election_keys(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    election_id INTEGER REFERENCES election(id),
    SK TEXT NOT NULL,
    PK TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS candidate_in_election(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    election_id INTEGER REFERENCES election(id),
    candidate_id INTEGER REFERENCES candidate(id),
    vote_number INTEGER NOT NULL
);

