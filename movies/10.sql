SELECT name FROM directors JOIN people ON id = person_id where movie_id = (
    SELECT movie_id FROM ratings WHERE rating >= 9.0);
