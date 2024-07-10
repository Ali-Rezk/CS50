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
