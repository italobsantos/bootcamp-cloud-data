CREATE KEYSPACE fenda_biquini WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

use fenda_biquini ;

CREATE COLUMNFAMILY clients (name TEXT PRIMARY KEY, age INT);
SELECT * FROM clients ;

INSERT INTO clients (name , age ) VALUES ( 'Bob Esponja', 38);
SELECT * FROM clients ;

INSERT INTO clients JSON '{"name": "Patrick"}';
SELECT * FROM clients ;

 SELECT age, WRITETIME(age) FROM clients;

 SELECT * FROM clients WHERE name = 'Bob Esponja';
SELECT JSON * from clients;

 UPDATE clients SET age = 33 WHERE name= 'Patrick';
SELECT * FROM clients ;

ALTER COLUMNFAMILY clients ADD hobby TEXT;
UPDATE clients SET hobby = 'Caçar Água Viva' WHERE name = 'Patrick';
SELECT age, WRITETIME(age), hobby, WRITETIME(hobby) FROM clients;

DELETE FROM clients WHERE name = 'Bob Esponja';