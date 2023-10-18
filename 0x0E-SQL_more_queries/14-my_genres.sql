-- Uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- Record displays tv_genres.name in ascending order
SELECT `tv_genre`.`name` FROM `tv_genre`
    INNER JOIN `tv_show_genres` ON `tv_genre`.`id` = `tv_show_genres`.`genre_id`
    INNER JOIN `tv_shows` ON `tv_shows`.`id` = `tv_show_genres`.`show_id`
WHERE `tv_shows`.`title` = `DEXTER`
ORDER BY `tv_genre`.`name` ASC;