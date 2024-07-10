SELECT DISTINCT *
FROM people
WHERE phone_number = (
    SELECT receiver
    FROM phone_calls
    WHERE receiver = '(375) 555-8161'
)
;
