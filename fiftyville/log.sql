-- getting the description of the crime.
SELECT description
FROM crime_scene_reports
WHERE day = 28 AND month = 7
AND year = 2023 AND street = 'Humphrey Street';
-- getting the transcript of the 3 witnesses.
SELECT transcript
FROM interviews
WHERE day = 28 AND month = 7
AND year = 2023;
--getting info about the car of the thief.
SELECT *
FROM bakery_security_logs
WHERE day = 28 AND month = 7
AND year = 2023 AND hour = 10
AND minute >= 15 AND minute <= 25;
--getting some info about the suspicious the transactions
SELECT *
FROM atm_transactions
WHERE day = 28 AND month = 7
AND year = 2023 AND atm_location = 'Leggett Street'
AND transaction_type = 'withdraw';
--getting info about the suspects
SELECT *
FROM bank_accounts
JOIN people ON person_id = id
WHERE account_number IN (28500762, 28296815, 76054385, 49610011, 16153065, 25506511, 81061156, 26013199);
--getting info about the phone calls that fit the description.
SELECT *
FROM phone_calls
WHERE day = 28 AND month = 7
AND year = 2023 AND duration < 60;
--identifying the earliest flight from fiftyville and its destination.
SELECT *
FROM flights
WHERE day = 29 AND month = 7
AND year = 2023;
--identifying the city the thief escaped to.
SELECT *
FROM airports
WHERE id IN (8, 4);
--getting passport numbers.
SELECT *
FROM passengers
WHERE flight_id = 36;
--identifying the thief.
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
--identifying the accomplice.
SELECT name
FROM people
WHERE phone_number = (
    SELECT receiver
    FROM phone_calls
    WHERE receiver = '(375) 555-8161'
);
