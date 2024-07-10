SELECT *
FROM airports
JOIN flights f ON origin_airport_id = f.id
WHERE day = 29 AND month = 7
AND year = 2023
;
