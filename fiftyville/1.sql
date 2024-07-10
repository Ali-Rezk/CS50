SELECT DISTINCT name, p1.license_plate, p1.phone_number, account_number, p1.passport_number
FROM people
WHERE phone_number = (
    SELECT reciever
    FROM phone_calls
    WHERE 
)
;
