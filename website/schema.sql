CREATE TABLE IF NOT EXISTS election(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS candidate (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    election_id INTEGER REFERENCES election(id),
    name TEXT NOT NULL,
    vote_numer INTEGER NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS voter_participation (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    election_id INTEGER REFERENCES election(id),
    fingerprint TEXT NOT NULL,
    vote_token TEXT NOT NULL,
    is_signed INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS result(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    election_id INTEGER REFERENCES election(id),
    candidate_id INTEGER REFERENCES candidate(id),
    vote_count INTEGER NOT NULL
);