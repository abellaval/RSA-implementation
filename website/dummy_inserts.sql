PRAGMA encoding='UTF-8';

-- Create elections
INSERT INTO election (name, description)
VALUES ('Couleurs', 'Saviez-vous que toutes les couleurs ont un symbolisme? Choisissez votre couleur préférée!'),
       ('Fruits', 'Choisissez le fruit que vous pourriez manger tous les jours!'),
       ('Musiques', 'Vous avez un style de musique préféré? Allez voter pour voir quel sera le style le plus populaire parmi les participants!'),
       ('Pays', 'Quelle est votre destination préférée pour les vacances d''été? '),
       ('Parcs', 'On profite du printemps! Choisissez le parc à Bruxelles que vous fréquentez le plus.'),
       ('7 Merveilles', 'Parmi les sept merveilles du monde antique, quelle est celle qui vous attire le plus?');

--source couleurs: https://www.toutes-les-couleurs.com/signification-des-couleurs.php
--source fruits: https://www.conservation-nature.fr/food/fruits/
--source musique: https://linkaband.com/blog-musique/culture/style-musique
--source pays: https://www.partir.com/ou-partir/juillet/soleil/voyage.html
--source parcs: https://visit.brussels/fr/lists/parcs-a-bruxelles
--source 7 merveilles:http://passerelles.bnf.fr/reperes/sept_merveilles_01.php

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
       ('Metal', 'Le heavy métal est un genre de musique rock qui n''est pas près de rouiller ! L''énergie dégagée par les furieux guitaristes, bassistes et batteurs du monde métal est juste phénoménale.'),
       ('Portugal','Au fil des étendues de sables infinies, villages de pêcheurs, nuits suaves et fado distillent le doux parfum des vacances.'),
       ('Canaries','Baignées par l''océan, façonnées par les vents et caressées par le soleil de juillet, les Canaries dessinent un miracle de diversité.'),
       ('Grèce','De sites antiques en îles paradisiaques, la beauté insolente de la Méditerranée éblouit tous les sens.'),
       ('Tunisie','Grand ciel bleu sur les sites archéologiques, les dunes, les oasis et les médinas qui se profilent, jamais bien loin du transat.'),
       ('Bahamas','Parce que ses eaux dessinent un rêve insulaire, parce que le soleil de juillet brille encore… et parce qu’on a qu’une vie.'),

       ('Parc Royale','Il offre de larges allées, des alignements symétriques et de surprenantes perspectives.'),
       ('Parc du Cinquantenaire','Le site est un vaste ensemble de jardins, ponctué de monuments et de musées. Il est dominé par un arc de triomphe à 3 arcades : le cinquantenaire. '),
       ('Bois de la Cambre','Ce parc aménagé à l''anglaise aux allures de forêt doit son nom à l''Abbaye de la Cambre, installée à proximité. Il s''agit d''un joyau unique du patrimoine bruxellois, qui n’a rien à envier à l''emblématique « Central Park » de New York.'),
       ('Etangs d''Ixelles','Lieux de promenade incontournable de Bruxelles, les Etangs d''Ixelles prolongent les jardins de l''Abbaye de la Cambre dans un quartier à la qualité architecturale indéniable.'),
       ('Parc Roi Baudouin','La découverte de biotopes très variés ou de sites naturels ou semi-naturels sont autant de bonnes raisons pour entreprendre la découverte de ce paradis vert du nord-ouest de Bruxelles.'),

       ('La pyramide de Khéops','Le tombeau du roi Khéops est la plus grande pyramide au monde avec sa base de 230 m de côté. Ses dimensions et sa masse de 500 000 tonnes expliquent sans doute que la pyramide de Khéops soit la seule merveille du monde antique que nous puissions encore admirer aujourd''hui.'),
       ('Les Jardins suspendus de Babylone','Organisés en terrasses, ces jardins auraient été construits par Nabuchodonosor II. Un ingénieux système d''acheminement de l''eau permettait de garder ces jardins toujours verts malgré l''aridité du pays alentour. '),
       ('La statue en or et ivoire de Zeus à Olympie','Cette gigantesque statue réalisée au Ve siècle avant J.-C. par le célèbre sculpteur athénien Phidias était faite de bois plaqué de deux matières précieuses entre toutes : l''or et l''ivoire.'),
       ('Le temple d''Artémis','Il était dédié à Artemis, déesse grecque de la nature et de la chasse. Construit entre le VIe et le Ve siècle avant J.-C., il offrait une architecture proche de celle du Parthénon d''Athènes. '),
       ('Le tombeau de Mausole','D''après l''écrivain latin Pline, le tombeau reposait sur une forme carrée se transformant en pyramide tronquée à mi-hauteur, et surmonté d''un char portant les époux royaux.'),
       ('Le colosse de Rhodes','Selon la légende et la plupart des représentations iconographiques, le colosse de Rhodes, haut de 30 m, constituait l''entrée du port de Rhodes. Les navires passaient entre ses jambes écartées pour entrer dans la ville.'),
       ('Le phare d''Alexandrie','Construit au IIIe siècle avant Jésus-Christ, le phare d''Alexandrie est l''une des sept merveilles du monde. Haut de plus de 100 m, il s''effondre et disparaît au XVe siècle, mais reste un modèle mythique dans l''esprit des constructeurs');

-- Associate candidates with an election
INSERT INTO candidate_in_election(election_id, candidate_id, vote_number)
VALUES (1, 1, 2),(1, 2, 3),(1, 3, 5),(1, 4, 7),(1, 5, 11),
       (2, 6, 2),(2, 7, 3),(2, 8, 5),(2, 9, 7),(2, 10, 11),
       (3, 11, 2),(3, 12, 3),(3, 13, 5),(3, 14, 7),(3, 15, 11),
       (4, 16, 2),(4, 17, 3),(4, 18, 5),(4, 19, 7),(4, 20, 11),
       (5, 21, 2),(5, 22, 3),(5, 23, 5),(5, 24, 7),(5, 25, 11),
       (6, 26, 2),(6, 27, 3),(6, 28, 5),(6, 29, 7),(6, 30, 11);

-- Create results for each election
INSERT INTO result(election_candidate_id, vote_count)
SELECT ce.id, 0
FROM candidate_in_election AS ce

