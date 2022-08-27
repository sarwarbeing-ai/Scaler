/*
Display the titles and popularity of the top 5
movies based on their popularity
which also belong to the 'Horror' genre.  */
SELECT
original_title,popularity
FROM movies
where genres="Horror"
order by popularity desc
limit 5
