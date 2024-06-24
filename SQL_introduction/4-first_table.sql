-- Script that creates a table called first_table in the current database in my MySQL server
-- If the table first_table already exists, my script should not fail

CREATE TABLE [IF NOT EXISTS] first_table (
	id INT,
	name VARCHAR(256),
);
