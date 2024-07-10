SELECT DISTINCT name, p1.license_plate, p1.phone_number, account_number, p1.passport_number
FROM people p1
JOIN bakery_security_logs b ON p1.license_plate = b.license_plate
JOIN phone_calls p2 ON p1.phone_number = p2.caller
JOIN passengers PS ON P1.passport_number = PS.passport_number
JOIN bank_accounts b2 ON p1.id = b2.person_id
WHERE duration < 60
AND b.day = 28 AND b.month = 7
AND b.year = 2023 AND hour = 10
AND minute >= 15 AND minute <= 25
AND flight_id = 36
AND account_number IN (28500762, 28296815, 76054385, 49610011, 16153065, 25506511, 81061156, 26013199);
