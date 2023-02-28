DROP DATABASE IF EXISTS library;

CREATE DATABASE IF NOT EXISTS library;

use library;

CREATE TABLE books
(
ID INT PRIMARY KEY NOT NULL auto_increment,
Title VARCHAR(50) NOT NULL,
Author VARCHAR(50) NOT NULL,
Publication_Year INT NOT NULL
);

INSERT INTO books VALUES (default, 'book about things', 'ann', 2001),
						(default, 'book about ladders', 'bob', 2006);