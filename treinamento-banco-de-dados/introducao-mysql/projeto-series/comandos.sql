CREATE TABLE movies(
    id INT PRIMARY KEY AUTO_INCREMENT,
    type INT,
    name VARCHAR(30) NOT NULL,
    total_ep INT,
    atual_ep INT,
    last_view DATE DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO `movies` (`id`, `type`, `name`, `total_ep`, `atual_ep`, `last_view`) VALUES (1, 0, 'Friends', 10, 1, current_timestamp())

INSERT INTO movies (id, type, name, last_view) VALUES (2, 1, 'Avengers', current_timestamp())

UPDATE `movies` SET `last_view` = '2022-04-01' WHERE `movies`.`id` = 1

INSERT INTO `movies` (`id`, `type`, `name`, `total_ep`, `atual_ep`, `last_view`) VALUES (3, 0, 'Todo mundo odeia o Chris', 20, 1, '2022-03-16'), (4, 1, '1917', NULL, NULL, current_timestamp())

SELECT * FROM movies WHERE id = 4
DELETE FROM movies WHERE id = 4

INSERT INTO `movies` ( `type`, `name`, `total_ep`, `atual_ep`, `last_view`) VALUES ( 1, '1917', NULL, NULL, current_timestamp())
