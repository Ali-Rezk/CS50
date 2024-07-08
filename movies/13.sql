SELECT name
FROM stars
JOIN people p ON person_id = p.id
JOIN movies m ON movie_id = m.id
WHERE person_id = (
    SELECT id FROM people WHERE name = 'Kevin Bacon' AND birth = 1958
)
;
