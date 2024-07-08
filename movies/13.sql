SELECT name
FROM stars
JOIN people ON person_id = id
WHERE movie_id = (
    SELECT id FROM stars WHERE person_id = (
        SELECT id FROM people WHERE name = 'Kevin Bacon' AND birth = 1958
    )
)
;
