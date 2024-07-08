SELECT title
FROM movies
JOIN stars s1 ON movies.id = s1.movie_id
JOIN stars s2 ON movies.id = s2.movie_id
JOIN people p1 ON movies.id = people.id
JOIN people p2 ON s2.person_id = people.id
WHERE name = 'Bradley Cooper' AND 'Jennifer Lawrence';
