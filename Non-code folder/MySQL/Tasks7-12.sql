# В подключенном MySQL репозитории создать базу данных “Друзья человека”
CREATE DATABASE 'Друзья человека';

# Создать таблицы с иерархией из диаграммы в БД
USE 'Друзья человека';

CREATE TABLE Dogs
(
    id INT,
    Name VARCHAR(45),
    TrainingCommands VARCHAR(45),
    DateOfBirth DATE
);

CREATE TABLE Cats
(
    id INT,
    Name VARCHAR(45),
    TrainingCommands VARCHAR(45),
    DateOfBirth DATE
);

CREATE TABLE Hamsters
(
    id INT,
    Name VARCHAR(45),
    TrainingCommands VARCHAR(45),
    DateOfBirth DATE
);

CREATE TABLE Horses
(
    id INT,
    Name VARCHAR(45),
    TrainingCommands VARCHAR(45),
    DateOfBirth DATE
);

CREATE TABLE Camels
(
    id INT,
    Name VARCHAR(45),
    TrainingCommands VARCHAR(45),
    DateOfBirth DATE
);

CREATE TABLE Donkeys
(
    id INT,
    Name VARCHAR(45),
    TrainingCommands VARCHAR(45),
    DateOfBirth DATE
);


# Заполнить низкоуровневые таблицы именами(животных), командами которые они выполняют и датами рождения
INSERT INTO Cats (id, Name, TrainingCommands, DateOfBirth)
VALUES(1001,'Fisa', 'sit down', date'2016-06-09'), (1002,'Gucci', 'jump', date'2023-03-11'), (1003,'Foxy', 'lie down',
date'2020-06-21');

INSERT INTO Dogs (id, Name, TrainingCommands, DateOfBirth)
VALUES(1004,'Sharik', 'attack', date'2015-06-30'), (1005, 'Sherkhan', 'Sit down', date'2021-12-11'), (1006,'Tapok',
'bite, run', date'2022-10-18');

INSERT INTO Hamsters (id, Name, TrainingCommands, DateOfBirth)
VALUES(1007,'Nolik', 'run', date'2023-08-08'), (1008, 'Nosok', 'come up', date'2022-12-11'), (1009, 'Kroha', 'jump', date'2022-01-02'), (1010, 'Luchik', 'run', date'2022-01-12');

INSERT INTO Horses (id, Name, TrainingCommands, DateOfBirth)
VALUES(1011,'Moonlight', 'run, go slowly', date'2019-09-25'), (1012, 'Saygak', 'come up', date'2017-09-21'), (1013,
'Kon', 'trot, escape', date'2015-11-15'), (1014, 'Flop', 'go slowly', date'2019-01-19'), (1015, 'Sessy', 'trot, run', date'2019-01-19');

INSERT INTO Camels (id, Name, TrainingCommands, DateOfBirth)
VALUES(1016,'Verblyud', 'trot', date'2015-08-11'), (1017, 'Camel', 'come up', date'2023-01-17');

INSERT INTO Donkeys (id, Name, TrainingCommands, DateOfBirth)
VALUES(1018,'Osel', 'run', date'2021-12-08'), (1019, 'Lishniy', 'go away', date'2018-06-11'), (1020, 'Ishak', 'come here, go', date'2021-01-01');

# Удалив из таблицы верблюдов, т.к. верблюдов решили перевезти в другой питомник на зимовку. Объединить таблицы Horses, и Donkeys в одну таблицу.
TRUNCATE TABLE Camels;

SELECT * FROM Horses
UNION SELECT * FROM Donkeys
AS 'Pack animals';

# Создать новую таблицу “молодые животные” в которую попадут все животные старше 1 года,
# но младше 3 лет и в отдельном столбце с точностью до месяца подсчитать возраст животных в новой таблице

CREATE TABLE 'Young of domestic animals'
SELECT id, Name, TrainingCommands, DateOfBirth,
(YEAR(CURRENT_DATE)-YEAR(DateOfBirth)) - (RIGHT(CURRENT_DATE,5)<RIGHT(DateOfBirth,5)) AS Возраст
FROM Dogs
WHERE (YEAR(CURRENT_DATE)-YEAR(DateOfBirth)) - (RIGHT(CURRENT_DATE,5)<RIGHT(DateOfBirth,5)) < 3
AND (YEAR(CURRENT_DATE)-YEAR(DateOfBirth)) - (RIGHT(CURRENT_DATE,5)<RIGHT(DateOfBirth,5)) > 1
UNION
SELECT id, Name, TrainingCommands, DateOfBirth,
(YEAR(CURRENT_DATE)-YEAR(DateOfBirth)) - (RIGHT(CURRENT_DATE,5)<RIGHT(DateOfBirth,5)) AS Возраст
FROM Cats
WHERE (YEAR(CURRENT_DATE)-YEAR(DateOfBirth)) - (RIGHT(CURRENT_DATE,5)<RIGHT(DateOfBirth,5)) < 3
AND (YEAR(CURRENT_DATE)-YEAR(DateOfBirth)) - (RIGHT(CURRENT_DATE,5)<RIGHT(DateOfBirth,5)) > 1
UNION
SELECT id, Name, TrainingCommands, DateOfBirth,
(YEAR(CURRENT_DATE)-YEAR(DateOfBirth)) - (RIGHT(CURRENT_DATE,5)<RIGHT(DateOfBirth,5)) AS Возраст
FROM Hamsters
WHERE (YEAR(CURRENT_DATE)-YEAR(DateOfBirth)) - (RIGHT(CURRENT_DATE,5)<RIGHT(DateOfBirth,5)) < 3
AND (YEAR(CURRENT_DATE)-YEAR(DateOfBirth)) - (RIGHT(CURRENT_DATE,5)<RIGHT(DateOfBirth,5)) > 1
UNION
SELECT id, Name, TrainingCommands, DateOfBirth,
(YEAR(CURRENT_DATE)-YEAR(DateOfBirth)) - (RIGHT(CURRENT_DATE,5)<RIGHT(DateOfBirth,5)) AS Возраст
FROM Horses
WHERE (YEAR(CURRENT_DATE)-YEAR(DateOfBirth)) - (RIGHT(CURRENT_DATE,5)<RIGHT(DateOfBirth,5)) < 3
AND (YEAR(CURRENT_DATE)-YEAR(DateOfBirth)) - (RIGHT(CURRENT_DATE,5)<RIGHT(DateOfBirth,5)) > 1
UNION
SELECT id, Name, TrainingCommands, DateOfBirth,
(YEAR(CURRENT_DATE)-YEAR(DateOfBirth)) - (RIGHT(CURRENT_DATE,5)<RIGHT(DateOfBirth,5)) AS Возраст
FROM Camels
WHERE (YEAR(CURRENT_DATE)-YEAR(DateOfBirth)) - (RIGHT(CURRENT_DATE,5)<RIGHT(DateOfBirth,5)) < 3
AND (YEAR(CURRENT_DATE)-YEAR(DateOfBirth)) - (RIGHT(CURRENT_DATE,5)<RIGHT(DateOfBirth,5)) > 1
UNION
SELECT id, Name, TrainingCommands, DateOfBirth,
(YEAR(CURRENT_DATE)-YEAR(DateOfBirth)) - (RIGHT(CURRENT_DATE,5)<RIGHT(DateOfBirth,5)) AS Возраст
FROM Donkeys
WHERE (YEAR(CURRENT_DATE)-YEAR(DateOfBirth)) - (RIGHT(CURRENT_DATE,5)<RIGHT(DateOfBirth,5)) < 3
AND (YEAR(CURRENT_DATE)-YEAR(DateOfBirth)) - (RIGHT(CURRENT_DATE,5)<RIGHT(DateOfBirth,5)) > 1
ORDER BY id;

# Объединить все таблицы в одну, при этом сохраняя поля, указывающие на прошлую принадлежность к старым таблицам.
SELECT DISTINCT *
FROM (SELECT * FROM Dogs
UNION ALL SELECT * FROM Cats
UNION ALL SELECT * FROM Hamsters
UNION ALL SELECT * FROM Horses
UNION ALL SELECT * FROM Camels
UNION ALL SELECT * FROM Donkeys)
AS 'All of domestic animals'
ORDER BY id;
