SELECT title FROM ((stars JOIN movies ON movie_id = movies.id) JOIN people ON person_id = people.id)
    WHERE name = 'Bradley Cooper' OR 'Jennifer Lawrence';
