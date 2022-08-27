/*
Show the details of the movie's original_title,
 director, genres, cast, budget, revenue, runtime,
 and vote_average which has keywords
like 'sport' or 'sequel' or 'suspense'. */
SELECT
original_title,
director,
genres,
cast,
budget,
revenue,
runtime,
vote_average
FROM movies
where keywords="sport" or  keywords="sequel" or  keywords="suspense";
