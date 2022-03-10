-- Create elections
INSERT INTO election (name, description)
VALUES ('Election 1', 'Description for election 1'),
       ('Election 2', 'Description for election 2'),
       ('Election 3', 'Description for election 3');

-- Create candidates
INSERT INTO candidate (name, description)
VALUES ('Candidate 1', 'Description for candidate 1'),
       ('Candidate 2', 'Description for candidate 2'),
       ('Candidate 3', 'Description for candidate 3'),
       ('Candidate 4', 'Description for candidate 4'),
       ('Candidate 5', 'Description for candidate 5'),
       ('Candidate 6', 'Description for candidate 6'),
       ('Candidate 7', 'Description for candidate 7'),
       ('Candidate 8', 'Description for candidate 8');

-- Associate candidates with an election
INSERT INTO candidate_in_election(election_id, candidate_id, vote_number)
VALUES (1, 1, 2),
       (1, 2, 3),
       (1, 3, 5),
       (2, 4, 2),
       (2, 5, 3),
       (3, 6, 2),
       (3, 7, 3),
       (3, 8, 5);

-- Create results for each election
INSERT INTO result(election_candidate_id, vote_count)
SELECT ce.id, 0
FROM candidate_in_election AS ce

