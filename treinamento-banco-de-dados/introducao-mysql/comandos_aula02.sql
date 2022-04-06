--Command Lines
CREATE TABLE cursos(id_curso INT NOT NULL PRIMARY KEY AUTO_INCREMENT, nome VARCHAR(20));

INSERT INTO cursos(nome) VALUES ('MySQL');
INSERT INTO cursos(nome) VALUES ('HTML');
INSERT INTO cursos(nome) VALUES ('CSS');

SELECT * FROM cursos;

UPDATE cursos SET nome='HTML 5' WHERE id_curso=2;

SELECT * FROM cursos;

INSERT INTO cursos(nome) VALUES ('Contabilidade');
SELECT * FROM cursos;

INSERT INTO cursos(nome) VALUES ('Economia');
SELECT * FROM cursos WHERE nome='Economia';
DELETE FROM cursos WHERE nome='Economia';

ALTER TABLE cursos ADD carga_horaria INT(2);

UPDATE cursos SET carga_horaria=20;
UPDATE cursos SET carga_horaria=10 WHERE id_curso = 2;

--Modelo Relacional
CREATE TABLE videos (
    id_video INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    author VARCHAR(30),
    title VARCHAR(30),
    likes INT,
    dislikes INT
);

INSERT INTO videos(author,title,likes,dislikes) VALUES ('Maria', 'MySQL', 10, 2);
INSERT INTO videos(author,title,likes,dislikes) VALUES ('João', 'HTML', 30, 1);
INSERT INTO videos(author,title,likes,dislikes) VALUES ('Maria', 'CSS', 18, 3);
INSERT INTO videos(author,title,likes,dislikes) VALUES ('Pedro', 'JavaScript', 15, 8);
INSERT INTO videos(author,title,likes,dislikes) VALUES ('Maria', 'Python', 50, 0);

CREATE TABLE author (
    id_author INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(30),
    born DATE,
);

INSERT INTO author(nome, born) VALUES ('Maria', '1992-04-10');
INSERT INTO author(nome, born) VALUES ('Pedro', '2000-10-12');
INSERT INTO author(nome, born) VALUES ('João', '1998-03-09');
INSERT INTO author(nome, born) VALUES ('Flavia', '2008-12-05');

UPDATE videos SET author= '';

UPDATE videos SET author=1 WHERE id_video = 1;
UPDATE videos SET author=1 WHERE id_video = 3;
UPDATE videos SET author=1 WHERE id_video = 5;
UPDATE videos SET author=2 WHERE id_video = 4;
UPDATE videos SET author=3 WHERE id_video = 2;

ALTER TABLE `videos` CHANGE `author` `fk_author` INT(11) NOT NULL;
ALTER TABLE `videos` ADD CONSTRAINT `fk_author` FOREIGN KEY (`fk_author`) REFERENCES `author`(`id_author`) ON DELETE CASCADE ON UPDATE CASCADE;

SELECT * FROM videos;
SELECT * FROM videos JOIN author ON videos.fk_author = author.id_author;

SELECT videos.title, author.nome FROM videos JOIN author ON videos.fk_author = author.id_author;

CREATE TABLE seo (
    id_seo INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    category VARCHAR(20) NOT NULL,
);

INSERT INTO videos(fk_author, title, likes, dislikes) VALUES (2,'PHP',20, 8);

INSERT INTO seo(category) VALUES ('Frontend');
INSERT INTO seo(category) VALUES ('Backend');

ALTER TABLE `videos` ADD `fk_seo` INT NOT NULL AFTER `title`;

UPDATE videos SET fk_seo=1 WHERE id_video = 2;
UPDATE videos SET fk_seo=1 WHERE id_video = 3;
UPDATE videos SET fk_seo=1 WHERE id_video = 4;
UPDATE videos SET fk_seo=2 WHERE id_video = 1;
UPDATE videos SET fk_seo=2 WHERE id_video = 5;
UPDATE videos SET fk_seo=2 WHERE id_video = 6;

ALTER TABLE `videos` ADD CONSTRAINT `fk_seo` FOREIGN KEY (`fk_seo`) REFERENCES `seo`(`id_seo`) ON DELETE CASCADE ON UPDATE CASCADE;

SELECT * FROM videos JOIN seo ON videos.fk_seo = seo.id_seo;
SELECT videos.title, seo.category FROM videos JOIN seo ON videos.fk_seo = seo.id_seo;

SELECT videos.title, author.nome, seo.category FROM videos JOIN seo ON videos.fk_seo = seo.id_seo
JOIN author ON videos.fk_author = author.id_author;

--Relacionamento muitos para muitos

CREATE TABLE playlist (
    id_playlist INT NOT NULL PRIMARY KEY AUTO_INCREMENT ,
    name_pl VARCHAR(30) NOT NULL
);

INSERT INTO playlist(name_pl) VALUES ('HTML + CSS');
INSERT INTO playlist(name_pl) VALUES ('HTML + PHP + JS');
INSERT INTO playlist(name_pl) VALUES ('Python + PHP');

CREATE TABLE videos_playlist (
    id_vp INT NOT NULL PRIMARY KEY AUTO_INCREMENT , 
    fk_videos INT NOT NULL ,
    fk_playlist INT NOT NULL
);

INSERT INTO videos_playlist(fk_videos,fk_playlist) VALUES (2, 1);
INSERT INTO videos_playlist(fk_videos,fk_playlist) VALUES (3, 1);
INSERT INTO videos_playlist(fk_videos,fk_playlist) VALUES (2, 2);
INSERT INTO videos_playlist(fk_videos,fk_playlist) VALUES (6, 2);
INSERT INTO videos_playlist(fk_videos,fk_playlist) VALUES (4, 2);
INSERT INTO videos_playlist(fk_videos,fk_playlist) VALUES (5, 3);
INSERT INTO videos_playlist(fk_videos,fk_playlist) VALUES (6, 3);

SELECT * FROM playlist JOIN videos_playlist ON playlist.id_playlist = videos_playlist.fk_playlist;

SELECT * FROM playlist JOIN videos_playlist ON playlist.id_playlist = videos_playlist.fk_playlist
JOIN videos ON videos.id_video = videos_playlist.fk_videos;

SELECT playlist.name_pl, videos.title FROM playlist 
JOIN videos_playlist ON playlist.id_playlist = videos_playlist.fk_playlist
JOIN videos ON videos.id_video = videos_playlist.fk_videos;

SELECT playlist.name_pl, videos.title, author.nome FROM playlist 
JOIN videos_playlist ON playlist.id_playlist = videos_playlist.fk_playlist
JOIN videos ON videos.id_video = videos_playlist.fk_videos
JOIN author ON videos.fk_author = author.id_author;