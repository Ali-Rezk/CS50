SELECT name
FROM stars
JOIN people p ON person_id = id
WHERE person_id = (
    SELECT id FROM people WHERE name = 'Kevin Bacon' AND birth = 1958
)
AND movie_id = (
    
)
;
