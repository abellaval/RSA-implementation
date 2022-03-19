PRAGMA encoding='UTF-8';

-- Create elections
INSERT INTO election (name, description)
VALUES ('La meilleure couleur', 'Choisissez votre couleur préférée!'),
       ('Le meilleur fruit', 'Choisissez le fruit que vous pourriez manger tous les jours!'),
       ('La meilleure musique', 'Vous avez un style de musique préféré? Allez voter pour voir quel sera le style le plus populaire parmi les participants!');

--source couleurs: https://www.toutes-les-couleurs.com/signification-des-couleurs.php
--source fruits: https://www.conservation-nature.fr/food/fruits/
--source musique: https://linkaband.com/blog-musique/culture/style-musique

-- Create candidates
INSERT INTO candidate (name, description)
VALUES ('Bleu', 'La couleur bleue nous rappelle tout d''abord la nature et l''infini puisqu elle nous fait penser directement à la mer et au ciel. Le bleu est une couleur qui symbolise la paix, le calme, la sérénité, la fraîcheur mais aussi la sensibilité.'),
       ('Vert', 'Le vert est une couleur qui fait penser à la nature, c''est pourquoi il représente le naturel, l''équilibre, la permission et la fraicheur mais il peut également symboliser le bonheur, l''harmonie, la réussite, l''énergie, l''optimisme, la jeunesse, le calme, la sérénité.'),
       ('Violet', 'Le violet est une couleur qui symbolise la subtilité, le mystère, le romantisme, l''idéalisme, la protection et mélancolie. Il symbolise aussi la fraicheur, la pureté, la paix et luxe.'),
       ('Rouge', 'Le rouge est une couleur qui a du tempérament. Elle peut symboliser plusieurs valeurs contradictoires en même temps comme l''amour et la haine, la vie et la mort. Elle représente également la passion, la tentation, le feu, le sang, l''interdit, l''émotion, la colère, l''agressivité, la force, le pouvoir, la puissance, le luxe, l''énergie, la persévérance, le combat et la détermination.'),
       ('Noir', 'Le noir est une couleur terne qui symbolise des valeurs plutôt négatives. Le noir nous fait penser à la peur, à l''angoisse, à l''inconnu, à la perte, au vide et à la mort.'),
       ('Ananas', 'L''ananas est un fruit tropical cultivé aux Philippines, dans les Antilles, en Chine et en Thaïlande. Il est riche en vitamines et oligo-éléments.'),
       ('Banane', 'Essentiellement exportée par l''Afrique, l''Amérique Centrale et l''Amérique Latine, elle peut être consommée crue ou cuite'),
       ('Fraise', 'Riche en vitamines et en fibres, sa chair est tendre, juteuse et sucrée et se consomme crue ou cuite.'),
       ('Orange', 'L''orange est un agrume qui se consomme crue ou en jus. Sous sa peau brillante et rugueuse se trouve une pulpe dense, orange et parfumée, délicieusement sucrée et riche en vitamine C.'),
       ('Pomme', 'La pomme est un fruit peu calorique, chargée d''eau et de fibres. Sa fine peau cache une chair consistante qui se consomme crue, cuite ou en jus.'),
       ('Rock', 'Ce genre populaire est la révolution culturelle des années 40. Il s''inspire fortement du jazz, du blues et de la musique country.'),
       ('Pop', 'Le style est aujourd’hui le plus populaire à l''échelle mondiale. Au sommet des charts, le mouvement est porté par des titans de l''industrie musicale confortablement installés sur le trône !'),
       ('Jazz', 'La musique classique de l''Amérique ! Des notes de swing et blues, des voix d''appel et de réponse, des polyrythmies, et bien sûr, de l''improvisation'),
       ('Rap', 'Un flow de rimes cinglantes pour des messages percutants ! Ou tout simplement une belle histoire énoncée tel un discours sur des airs variés. Le rap est l''ingrédient principal de la musique urbaine et de la culture moderne.'),
       ('Metal', 'Le heavy métal est un genre de musique rock qui n''est pas près de rouiller ! L''énergie dégagée par les furieux guitaristes, bassistes et batteurs du monde métal est juste phénoménale.');

-- Associate candidates with an election
INSERT INTO candidate_in_election(election_id, candidate_id, vote_number)
VALUES (1, 1, 2),
       (1, 2, 3),
       (1, 3, 5),
       (1, 4, 7),
       (1, 5, 11),
       (2, 6, 2),
       (2, 7, 3),
       (2, 8, 5),
       (2, 9, 7),
       (2, 10, 11),
       (3, 11, 2),
       (3, 12, 3),
       (3, 13, 5),
       (3, 14, 7),
       (3, 15, 11);

-- Create results for each election
INSERT INTO result(election_candidate_id, vote_count)
SELECT ce.id, 0
FROM candidate_in_election AS ce

