-- Lists all Comedy shows in the database hbtn_0d_tvshows.
-- Record displays tv_shows.title in ascending order
SELECT `tv_shows`.`title` FROM `tv_shows`
    INNER JOIN `tv_show_genres` ON `tv_shows`.`id` = `tv_show_genres`.`show_id`
    INNER JOIN `tv_genre` ON `tv_genre`.`id` = `tv_show_genres`.`genre_id`
WHERE `tv_genre`.`name` = `Comedy`
ORDER BY `tv_shows`.`title` ASC;