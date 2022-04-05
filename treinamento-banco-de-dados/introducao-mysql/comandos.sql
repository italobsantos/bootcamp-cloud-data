CREATE TABLE pessoa(
    id INT NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(30) NOT NULL,
    nascimento DATE
);

INSERT INTO pessoa(nome, nascimento) VALUES('Italo', '1997-01-28');
INSERT INTO pessoa(nome, nascimento) VALUES('João', '2000-04-08');
INSERT INTO pessoa(nome, nascimento) VALUES('Lucas', '1985-05-31');

SELECT * FROM pessoa;
SELECT nome FROM pessoa;
SELECT nascimento FROM pessoa;

UPDATE pessoa SET nome = 'Italo Barbosa Santos';
UPDATE pessoa SET nome = 'João' WHERE id = 2;
UPDATE pessoa SET nome = 'Lucas' WHERE id = 3;

SELECT * FROM pessoa WHERE id = 3;
DELETE FROM pessoa WHERE id = 3;

SELECT * FROM pessoa ORDER BY nome;
SELECT * FROM pessoa ORDER BY nome DESC;

INSERT INTO pessoa(nome, nascimento) VALUES('Tamires', '1996-12-13');
ALTER TABLE 'pessoa' ADD 'genero' VARCHAR(1) NOT NULL AFTER 'nascimento'; 
UPDATE pessoa SET genero = 'M' WHERE id = 1;
UPDATE pessoa SET genero = 'M' WHERE id = 2;
UPDATE pessoa SET genero = 'M' WHERE id = 3;
UPDATE pessoa SET genero = 'F' WHERE id = 4;
SELECT genero FROM pessoa GROUP BY genero
SELECT COUNT(ID), genero FROM pessoa GROUP BY genero