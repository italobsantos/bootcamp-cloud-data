-- Comandos fornecidos pelo instrutor:
CREATE TABLE `canais` (
  `id_canal` int(11) NOT NULL,
  `nome_canal` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `canais` (`id_canal`, `nome_canal`) VALUES
(1, 'React'),
(2, 'PHP'),
(3, 'CSS'),
(4, 'HTML');

CREATE TABLE `videos` (
  `id_video` int(11) NOT NULL,
  `nome_video` varchar(100) NOT NULL,
  `autor_video` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `videos` (`id_video`, `nome_video`, `autor_video`) VALUES
(1, 'Login com React', 'React'),
(2, 'Componentes com React', 'React'),
(3, 'Listas com PHP', 'PHP'),
(4, 'Funções com PHP', 'PHP'),
(5, 'Páginas com HTML', 'HTML');

CREATE TABLE `videos_canais` (
  `id_canais_video` int(11) NOT NULL,
  `fk_canal` int(11) NOT NULL,
  `fk_video` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `videos_canais` (`id_canais_video`, `fk_canal`, `fk_video`) VALUES
(1, 2, 4),
(2, 2, 3),
(3, 1, 1),
(4, 1, 2),
(5, 4, 5);

ALTER TABLE `canais`
ADD PRIMARY KEY (`id_canal`);

ALTER TABLE `videos`
ADD PRIMARY KEY (`id_video`);

ALTER TABLE `videos_canais`
  ADD PRIMARY KEY (`id_canais_video`),
  ADD KEY `fk_canal` (`fk_canal`),
  ADD KEY `fk_video` (`fk_video`);

ALTER TABLE `canais`
  MODIFY `id_canal` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

ALTER TABLE `videos`
  MODIFY `id_video` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

ALTER TABLE `videos_canais`
  MODIFY `id_canais_video` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

ALTER TABLE `videos_canais`
  ADD CONSTRAINT `fk_canal` FOREIGN KEY (`fk_canal`) REFERENCES `canais` (`id_canal`),
  ADD CONSTRAINT `fk_video` FOREIGN KEY (`fk_video`) REFERENCES `videos` (`id_video`);
COMMIT;


-- Comandos criados durante as aulas:

SELECT * FROM videos_canais JOIN videos;
SELECT * FROM videos_canais JOIN videos ON videos_canais.fk_canal = videos.id_video;
SELECT * FROM videos_canais as vc JOIN videos as v ON vc.fk_canal = v.id_video;

SELECT * FROM videos_canais as vc JOIN videos as v ON vc.fk_canal = v.id_video
JOIN canais AS c ON vc.fk_canal = c.id_canal;

SELECT v.nome_video, v.autor_video, c.nome_canal FROM videos_canais as vc JOIN videos as v ON vc.fk_canal = v.id_video
JOIN canais AS c ON vc.fk_canal = c.id_canal;

SELECT * FROM videos_canais as vc 
LEFT OUTER JOIN videos as v ON vc.fk_canal = v.id_video

SELECT * FROM videos_canais as vc 
RIGHT OUTER JOIN videos as v ON vc.fk_canal = v.id_video

SELECT * FROM videos_canais as vc 
RIGHT OUTER JOIN videos as v ON vc.fk_canal = v.id_video
RIGHT OUTER JOIN canais as c ON vc.fk_canal = c.id_canal;

SELECT * FROM videos_canais as vc 
RIGHT OUTER JOIN videos as v ON vc.fk_canal = v.id_video
LEFT OUTER JOIN canais as c ON vc.fk_canal = c.id_canal;

SELECT v.id_video, v.nome_video FROM videos as v 
LEFT OUTER JOIN videos_canais as vc ON v.id_video = vc.fk_video
UNION
SELECT c.id_canal, c.nome_canal FROM videos_canais AS vc 
RIGHT OUTER JOIN canais as c ON vc.fk_canal = c.id_canal;