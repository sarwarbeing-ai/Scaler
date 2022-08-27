/*
Show the titles of the movies that are released after
2014 and have an average
vote rating greater than 7. */
SELECT
original_title
FROM movies
where release_year>2014 AND vote_average>7;
