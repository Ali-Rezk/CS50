SELECT *
FROM people
JOIN bank_accounts ON id = person_id
WHERE account_number IN (28500762, 28296815, 76054385, 49610011, 16153065, 25506511, 81061156, 26013199)
AND phone_number = (
    SELECT caller
    FROM phone_calls
    WHERE day = 28 AND month = 7
    AND year = 2023 AND duration < 60
)
AND license_plate = (
    SELECT license_plate
    FROM bakery_security_logs
    WHERE day = 28 AND month = 7
    AND year = 2023 AND hour = 10
    AND minute >= 15 AND minute <= 25
    )
AND passport_number = (
    SELECT passport_number
    FROM passengers
    WHERE flight_id = 36
)
;
