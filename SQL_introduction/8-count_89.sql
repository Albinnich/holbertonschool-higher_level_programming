-- Script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server
-- The database name will be passed as an argument of the mysql command

SELECT SUM(id = 89) FROM INFORMATION_SCHEMA.TABLES WHERE
TABLE_SCHEMA = 'first_table';
