SELECT *
FROM people p
JOIN bakery_security_logs b ON p.license_plate = b.license_plate
WHERE day = 28 AND month = 7
AND year = 2023 AND hour = 10
AND minute >= 15 AND minute <= 25
;
