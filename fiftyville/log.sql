-- getting the ids of the suspects result = 295, 297.
SELECT id
FROM crime_scene_reports c1
WHERE day = 28 AND month = 7
AND year = 2023 AND street = 'Humphrey Street';

