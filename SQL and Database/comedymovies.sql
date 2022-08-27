/*
Find all the movie titles and their cast that belongs to the
 'Comedy' genre using the movies table.*/
 SELECT
original_title,
cast
FROM movies
where genres="Comedy";
