/*
Find all the titles of the movies, cast, and
genres that are released between
the years 2012-2015(Including 2015). */
SELECT
original_title
FROM movies
where release_year BETWEEN 2012 AND 2015;
