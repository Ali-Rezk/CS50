-- getting the description of the crime.
SELECT description
FROM crime_scene_reports
WHERE day = 28 AND month = 7
AND year = 2023 AND street = 'Humphrey Street';
-- getting the name and transcript of the 3 witnesses.
SELECT name, transcript
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
--getting info about the phone calls that fit the description
SELECT *
FROM phone_calls
WHERE day = 28 AND month = 7
AND year = 2023 AND duration < 60;
--getting the ids of airports
SELECT *
FROM flights
WHERE day = 29 AND month = 7
AND year = 2023;
