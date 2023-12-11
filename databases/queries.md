Make sure you download the starter code and run the following:

```sh
  psql < movies.sql
  psql movies_db
```

In markdown, you can place a code block inside of three backticks (```) followed by the syntax highlighting you want, for example

\```sql

SELECT \* FROM users;

\```

Using the `movies_db` database, write the correct SQL queries for each of these tasks:

1.  The title of every movie.

```
 SELECT title FROM movies;
 ```

2.  All information on the G-rated movies.

```
SELECT a.title, a.release_year, a.runtime, a.rating, b.name AS studio
FROM movies a, studios b
WHERE a.studio_id = b.id 
AND a.rating = 'G';
```

3.  The title and release year of every movie, ordered with the
    oldest movie first.
    
```
SELECT title, release_year FROM movies
ORDER by release_year;
```
    
4.  All information on the 5 longest movies.

```
SELECT a.title, a.release_year, a.runtime, a.rating, b.name as studio
FROM movies a, studios b
WHERE a.studio_id = b.id 
ORDER BY runtime desc
LIMIT 5;
```

5.  A query that returns the columns of `rating` and `total`,       tabulating the
    total number of G, PG, PG-13, and R-rated movies.

```
SELECT rating, count(*) AS total
FROM movies
GROUP BY rating;
```

6.  A table with columns of `release_year` and `average_runtime`,
    tabulating the average runtime by year for every movie in the database. The data should be in reverse chronological order (i.e. the most recent year should be first).

```
SELECT release_year, AVG(runtime)
FROM movies
GROUP BY release_year
ORDER BY release_year desc;
```    

7.  The movie title and studio name for every movie in the
    database.

```
SELECT a.title,b.name AS "studio name"
FROM movies a, studios b
WHERE a.studio_id = b.id;
```

8.  The star first name, star last name, and movie title for every
    matching movie and star pair in the database.

```
 SELECT a.first_name, a.last_name, b.title AS "movie title" 
 FROM stars a, movies b , roles c 
 WHERE a.id = c.star_id
 AND b.id = c.movie_id;
```

9.  The first and last names of every star who has been in a G-rated movie. The first and last name should appear only once for each star, even if they are in several G-rated movies. *IMPORTANT NOTE*: it's possible that there can be two *different* actors with the same name, so make sure your solution accounts for that.

```
SELECT a.first_name, a.last_name, count(*) AS "num of G movies"
FROM stars a, movies b , roles c 
WHERE a.id = c.star_id AND b.id = c.movie_id
AND b.rating = 'G'
GROUP BY a.first_name, a.last_name;
```

10. The first and last names of every star along with the number
    of movies they have been in, in descending order by the number of movies. (Similar to #9, make sure
    that two different actors with the same name are considered separately).

```
SELECT a.first_name, a.last_name, count(*) AS "num of movies"
FROM stars a, movies b , roles c
WHERE a.id = c.star_id AND b.id = c.movie_id
GROUP BY a.first_name, a.last_name ORDER BY count(*) DESC;
```    

### The rest of these are bonuses

11. The title of every movie along with the number of stars in
    that movie, in descending order by the number of stars.

```
SELECT b.title, count(*) AS "num of stars"
FROM movies b, stars a, roles c
WHERE b.id = c.movie_id AND a.id = c.star_id 
GROUP BY b.title 
ORDER by count(*) DESC;
```

12. The first name, last name, and average runtime of the five
    stars whose movies have the longest average.

```
SELECT a.first_name, a.last_name , AVG(b.runtime) AS "average runtime"
FROM stars a, movies b, roles c
WHERE a.id = c.star_id AND b.id=c.movie_id
GROUP BY a.first_name, a.last_name
ORDER BY AVG(b.runtime) desc
LIMIT 5;
```

13. The first name, last name, and average runtime of the five
    stars whose movies have the longest average, among stars who have more than one movie in the database.

```
SELECT a.first_name, a.last_name,AVG(b.runtime) AS "average runtime"
FROM stars a, movies b, roles c
WHERE a.id = c.star_id AND b.id=c.movie_id
GROUP BY a.first_name, a.last_name
HAVING count(c.movie_id) > 1
LIMIT 5;
```

14. The titles of all movies that don't feature any stars in our
    database.

```
SELECT b.title
FROM movies b
WHERE b.id NOT IN  (select movie_id FROM roles);


15. The first and last names of all stars that don't appear in any movies in our database.

```
SELECT a.first_name, a.last_name
FROM stars a
WHERE a.id NOT IN (SELECT star_id FROM roles);
```

16. The first names, last names, and titles corresponding to every
    role in the database, along with every movie title that doesn't have a star, and the first and last names of every star not in a movie.

```
SELECT a.first_name, a.last_name , b.title
FROM movies b
FULL JOIN roles c
ON b.id = c.movie_id
FULL JOIN stars a
ON a.id = c.star_id;
```
