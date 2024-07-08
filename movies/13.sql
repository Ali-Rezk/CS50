SELECT name
FROM stars
JOIN people ON person_id = id
WHERE person_id = (
    SELECT id FROM people WHERE name = 'Kevin Bacon'
)
;
