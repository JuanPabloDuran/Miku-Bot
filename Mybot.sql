CREATE DATABASE Mybot;

USE Mybot;

CREATE TABLE recomendaciones(
    Genero int(10) NOT NULL,
    Anime varchar(100) NOT NULL,
    Capitulos int(5) NOT NULL,
    Emision varchar(10) NOT NULL);


INSERT INTO recomendaciones (Genero, Anime, Capitulos, Emision)
VALUES (1, 'Dragon Ball Super', 131, 'Finalizado'),
(1, 'Dragon Ball Z', 291, 'Finalizado'),
(1, 'One Punch Man', 12, 'Finalizado'),
(7, 'Sword Art Online', 25, 'Finalizado'),
(7, 'Isekai wa smatphone to Tomo ni', 12, 'Finalizado'),
(3, 'Kamisama Hajimemashita KaKo-hen', 12, 'Finalizado'),
(4, 'Nichijou', 26, 'Finalizado'),
(4, 'Danshi Koukosei no Nichijou', 19, 'Finalizado'),
(4, 'Watamote', 12, 'Finalizado'),
(5, 'Knight´s & Magic', 12, 'Finalizado'),
(6, 'Pokemon', 1050, 'En emision'),
(8, 'Death Note', 37, 'Finalizado'),
(9, 'Los super campeones', 128, 'Finalizado'),
(9, 'Kuroko no Basket', 75, 'Finalizado'),
(2, 'Another', 13, 'Finalizado'),
(2, 'Corpse Party: Tortured Souls', 4, 'Finalizado'),
(2, 'Gakkoo Gurashi', 12, 'Finalizado'),
(2, 'Elfen Lied', 13, 'Finalizado');

SHOW TABLES;

SELECT * FROM Recomendaciones;

DESCRIBE Recomendaciones;

CREATE USER 'Hatsune' IDENTIFIED BY 'Miku';
GRANT ALL privileges ON `Mybot`.* TO 'Hatsune'@localhost;
FLUSH PRIVILEGES;
