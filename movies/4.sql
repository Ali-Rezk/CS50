SELECT COUNT(id) FROM movies WHERE id = (
SELECT movie_id FROM ratings WHERE rating = 10.0);


