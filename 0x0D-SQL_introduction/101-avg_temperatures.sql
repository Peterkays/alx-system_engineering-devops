-- displays the average temperature (Fahrenheit) 
-- by city ordered by temperature (descending).
SELECT `city`, AVG(`value`) AS `ave_tempt` 
FROM `temperatures` GROUP BY `city` ORDER BY `ave_tempt` DESC;