/*
Find all the titles of the movies, directors, and
genres with a runtime of less than 120 mins. */
SELECT
original_title,
director,
genres
FROM movies
where runtime<120;
