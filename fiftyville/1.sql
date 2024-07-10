SELECT DISTINCT name
FROM people p1
JOIN bakery_security_logs b ON p1.license_plate = b.license_plate
JOIN phone_calls p2 ON p1.phone_number = p2.caller
JOIN passengers ON 
WHERE duration < 60
AND b.day = 28 AND b.month = 7
AND b.year = 2023 AND hour = 10
AND minute >= 15 AND minute <= 25
AND flight_id = 36
;
