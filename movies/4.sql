SELECT title, rating, COUNT(rating) FROM ratings JOIN movies ON movie_id = id
WHERE rating = 10.0;
