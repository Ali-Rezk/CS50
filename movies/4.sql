SELECT *
FROM ratings r
JOIN movies m ON r.movie_id = m.id
WHERE r.rating = 10.0;
