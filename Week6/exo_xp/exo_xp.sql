-- Database: public

-- DROP DATABASE IF EXISTS public;

-- CREATE DATABASE public
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'French_France.1252'
--     LC_CTYPE = 'French_France.1252'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;
-- CREATE TABLE items(id_items SERIAL,
-- 				   libelle VARCHAR PRIMARY KEY,
-- 				   price NUMERIC NOT NULL
-- 				  )
-- INSERT INTO items (libelle, price) 
-- VALUES('Small Desk', 100),
-- ('Large desk', 300),
-- ('Fan', 80);
-- CREATE TABLE customers(id_customers SERIAL,
--  				   firstname VARCHAR NOT NULL,
--  				   lastname VARCHAR NOT NULL
--  				  )
-- INSERT INTO customers (firstname, lastname) 
-- VALUES('Greg', 'Jones'),
-- ('Sandra', 'Jones'),
-- ('Scott', 'Scott'),
-- ('Trevor', 'Green'),
-- ('Melanie', 'Johnson');
-- SELECT * FROM items;
-- SELECT * FROM items WHERE price>80;
-- SELECT * FROM items WHERE price<=300;
-- SELECT * FROM customers WHERE lastname='Smith';
-- Le résultat sera un table vide.
-- SELECT * FROM customers WHERE lastname='Jones';
SELECT * FROM customers WHERE firstname !='Scott';