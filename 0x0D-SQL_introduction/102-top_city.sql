-- displays the top 3 of cities temperature 
-- during July and August ordered by temperature (descending)
SELECT `city`, AVG(`value`) AS `avg_tempt` FROM `temperatures` 
WHERE `month` = 7 OR `month` = 8 GROUP BY `city` ORDER BY `ave_tempt` DESC LIMIT 3;