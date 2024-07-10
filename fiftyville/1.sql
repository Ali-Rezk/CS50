SELECT DISTINCT name
FROM people
WHERE phone_number = (
    SELECT reciever
    FROM phone_calls
    WHERE reciever = '(375) 555-8161'
)
;
