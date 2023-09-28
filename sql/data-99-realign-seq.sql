select setval('person_id_seq', max(id)) from person;
select setval('movieapp_movie_id_seq', max(id)) from movie;
