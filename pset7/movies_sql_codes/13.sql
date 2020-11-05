SELECT distinct(people.name) FROM STARS join people on stars.person_id = people.id where stars.movie_id IN
(select movie_id from people join stars on stars.person_id = people.id where birth = 1958 and name = 'Kevin Bacon')
and people.name != 'Kevin Bacon'