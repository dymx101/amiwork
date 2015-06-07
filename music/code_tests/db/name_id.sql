INSERT INTO raw_data (SELECT * FROM `table 8`);


INSERT INTO mood (name)  (SELECT DISTINCT mood FROM raw_data);
INSERT INTO genre (name) (SELECT DISTINCT genre FROM raw_data);
INSERT INTO artist (name)  (SELECT DISTINCT artist FROM raw_data);

INSERT INTO tracks ( artistid,name,genre,mood ) (
	SELECT DISTINCT artist.id AS artistid, raw_data.title as title FROM raw_data JOIN artist JOIN genre JOIN mood ON artist.name=raw_data.artist AND raw_data.mood=mood.name AND raw_data.genre=genre.name
);


INSERT INTO tracks ( artistid,name) (SELECT DISTINCT artist.id AS artistid, raw_data.title as title FROM raw_data JOIN artist ON artist.name=raw_data.artist );
INSERT INTO track_genre(trackid,genreid) (SELECT DISTINCT tracks.id,genre.id FROM tracks JOIN raw_data JOIN genre ON tracks.name=raw_data.title AND raw_data.genre =genre.name);
INSERT INTO track_mood(trackid,moodid) (SELECT DISTINCT tracks.id,mood.id FROM tracks JOIN raw_data JOIN mood ON tracks.name=raw_data.title AND raw_data.mood =mood.name);