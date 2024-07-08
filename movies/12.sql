SELECT title FROM ((movies JOIN stars ON movies.id = movie_id) JOIN people ON person_id = people.id)
    WHERE name = 'Bradley Cooper' AND 'Jennifer Lawrence';
