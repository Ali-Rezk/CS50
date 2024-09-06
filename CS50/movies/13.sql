SELECT DISTINCT p2.name
FROM stars s1
JOIN people p1 ON s1.person_id = p1.id
JOIN stars s2 ON s1.movie_id = s2.movie_id
JOIN people p2 ON s2.person_id = p2.id
WHERE p1.name = 'Kevin Bacon'
AND p1.birth = 1958
AND p2.name != 'Kevin Bacon';