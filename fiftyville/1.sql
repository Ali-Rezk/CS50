SELECT *
FROM people p
JOIN bakery_security_logs b ON p.license_plate = b.license_plate
JOIN atm_transactions ON
WHERE day = 28 AND month = 7
AND year = 2023 AND atm_location = 'Leggett Street'
AND transaction_type = 'withdraw';
WHERE day = 28 AND month = 7
AND year = 2023 AND hour = 10
AND minute >= 15 AND minute <= 25
;
