DROP TABLE IF EXISTS raw_data;
CREATE TABLE raw_data(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT ,
	userid INT UNSIGNED,
	title VARCHAR(100),
	artist VARCHAR(100),
	mood VARCHAR(100),
	genre VARCHAR(100)
);


DROP TABLE IF EXISTS tracks;
CREATE TABLE tracks(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT ,
	artistid INT UNSIGNED,
	name VARCHAR(100),
	UNIQUE artist_track(artistid,name)
);
--mood INT UNSIGNED,
--genre INT UNSIGNED,
	

CREATE TABLE track_genre(
	trackid INT UNSIGNED,
	genreid INT UNSIGNED,
	PRIMARY KEY (trackid,genreid)
);


CREATE TABLE track_mood(
	trackid INT UNSIGNED,
	moodid INT UNSIGNED,
	PRIMARY KEY (trackid,moodid)
);

DROP TABLE IF EXISTS artist;
CREATE TABLE artist(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT ,
	name VARCHAR(100) UNIQUE
);

DROP TABLE IF EXISTS mood;
CREATE TABLE mood(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT ,
	name VARCHAR(100) UNIQUE
);


DROP TABLE IF EXISTS genre;
CREATE TABLE genre(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT ,
	name VARCHAR(100) UNIQUE
);

DROP TABLE IF EXISTS tempo;
CREATE TABLE tempo(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT ,
	name VARCHAR(100) UNIQUE
);


DROP TABLE IF EXISTS node;
CREATE TABLE node(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT ,
	nodetype ENUM('root','genre','mood','tempo','track','artist','user'),
	nodeid INT UNSIGNED, 		-- id of the genre/mood/tempo/track/artist/user[/...]
	parentid INT UNSIGNED,		-- id of the parent node
	support INT,
	UNIQUE node_type_id(nodetype,nodeid),
    INDEX parentid(parentid) 
);
