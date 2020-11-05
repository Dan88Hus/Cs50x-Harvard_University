select movies.title from people  join stars on stars.person_id = people.id join movies on movies.id = stars.movie_id
where people.name = 'Helena Bonham Carter'
intersect
select movies.title from people  join stars on stars.person_id = people.id join movies on movies.id = stars.movie_id
where people.name = 'Johnny Depp'
