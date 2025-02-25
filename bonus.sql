-- 7.2 Retrieve all movies that have ARMAGEDDON in their title and have a duration longer than 100 minutes
-- Hint: use `LIKE` operator. More information here: https://www.w3schools.com/sql/sql_like.asp
SELECT * FROM film 
WHERE title LIKE '%ARMAGEDDON%' 
AND length > 100;

-- 7.3 Determine the number of films that include Behind the Scenes content
SELECT COUNT(*) AS films_with_behind_the_scenes 
FROM film 
WHERE special_features LIKE '%Behind the Scenes%';