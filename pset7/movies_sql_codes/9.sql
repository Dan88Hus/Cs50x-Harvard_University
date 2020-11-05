select name from people join stars on people.id = stars.person_id join movies on movies.id = stars.movie_id
where movies.year = 2004 group by name, stars.person_id order by birth