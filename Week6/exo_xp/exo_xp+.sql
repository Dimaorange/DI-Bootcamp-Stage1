-- Database: bootcamp

-- DROP DATABASE IF EXISTS bootcamp;

-- CREATE DATABASE bootcamp
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'French_France.1252'
--     LC_CTYPE = 'French_France.1252'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;
-- CREATE TABLE students(id SERIAL PRIMARY KEY,
-- 					  first_name VARCHAR NOT NULL,
-- 					  last_name VARCHAR NOT NULL,
-- 					 birth_date DATE NOT NULL)
-- INSERT INTO students (first_name, last_name, birth_date) 
-- VALUES ('Marc','Benichou', '02/11/1998'),
-- ('Yoan', 'Cohen', '03/12/2010'),
-- ('Lea', 'Benichou',	'27/07/1987'),
-- ('Amelia', 'Dux', '07/04/1996'),
-- ('David', 'Grez', '14/06/2003'),
-- ('Omer', 'Simpson',' 03/10/1980'),
-- ('Issa','Dima', '23/08/1999');
-- SELECT * FROM students;
-- SELECT * FROM students WHERE id=2;
-- SELECT * FROM students WHERE last_name='Benichou' AND first_name='Marc';
-- SELECT * FROM students WHERE last_name='Benichou' OR first_name='Marc';
-- SELECT * FROM students WHERE first_name LIKE '%a%';
-- SELECT * FROM students WHERE first_name LIKE '%a';
-- SELECT * FROM students WHERE first_name LIKE '%a_';
-- SELECT * FROM students WHERE id=1 AND id=3;
-- SELECT * FROM students WHERE birth_date>='1/01/2000';