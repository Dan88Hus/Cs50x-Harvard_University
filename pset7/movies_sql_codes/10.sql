select distinct(name) from people join directors on people.id = directors.person_id join ratings on ratings.movie_id = directors.movie_id where ratings.rating >= '9.0'