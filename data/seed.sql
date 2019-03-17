drop table if exists user;
drop table if exists recipe;
drop table if exists cocktail;

create table recipe (
	id integer primary key autoincrement,
	user_id integer,
	title text NOT NULL,
	image_URL text NOT NULL,
	desription text NOT NULL,
	ingredients text NOT NULL,
	CONSTRAINT "fk_recipe_user" FOREIGN KEY("user_id") REFERENCES "user"("user_id") ON DELETE NO ACTION ON UPDATE CASCADE
);
create table user (
user_id INTEGER primary key AUTOINCREMENT,
username text NOT NULL,
password text NOT NULL
);

-- create table user (
--  ... ?
-- );

-- create table recipe (
-- ... ?
-- );

-- insert into user 
-- ... ?