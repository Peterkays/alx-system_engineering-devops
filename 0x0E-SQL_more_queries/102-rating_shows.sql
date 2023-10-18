-- Lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Record displays tv_shows.title - rating sum in descending order of the rating
SELECT `tv_shows`.`title`, SUM(`rate`) AS `rating` FROM `tv_shows`
    INNER JOIN `tv_show_ratings`
    ON `tv_shows`.`id` = `tv_show_ratings`.`show_id`
GROUP BY `tv_shows`.`title`
ORDER BY `rating` DESC;
