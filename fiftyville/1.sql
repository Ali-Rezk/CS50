SELECT *
FROM people
WHERE phone_number = (
    SELECT caller
    FROM phone_calls
    WHERE day = 28 AND month = 7
    AND year = 2023 AND duration < 60;
)
OR (
    SELECT receiver
    FROM phone_calls
    WHERE day = 28 AND month = 7
    AND year = 2023 AND duration < 60;
)
;
