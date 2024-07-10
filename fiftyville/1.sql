SELECT *
FROM people
SELECT *
FROM bank_accounts
JOIN people ON person_id = id
WHERE account_number IN (28500762, 28296815, 76054385, 49610011, 16153065, 25506511, 81061156, 26013199);
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
