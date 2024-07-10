SELECT name
FROM people p1
JOIN bakery_security_logs b ON p.license_plate = b.license_plate
JOIN atm_transactions a ON p.day = a.day
JOIN phone_calls p2 ON p1.phone_number = p2.caller
WHERE duration < 60
AND P1.day = 28 AND month = 7
AND year = 2023 AND hour = 10
AND minute >= 15 AND minute <= 25
AND atm_location = 'Leggett Street'
AND transaction_type = 'withdraw'
;
