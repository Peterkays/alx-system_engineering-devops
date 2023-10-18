-- Lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
-- Record displays tv_shows.title - tv_genres.name in ascending order
SELECT `tv_shows`.`title`, `tv_genres`.`name` FROM `tv_shows`
    LEFT OUTER JOIN `tv_show_genre` 
        ON `tv_shows`.`id` = `tv_show_genre`.`show_id`
    LEFT OUTER JOIN `tv_genres`
        ON `tv_genres`.`id` = `tv_show_genre`.`genre_id`
ORDER BY `tv_shows.title`, `tv_genres.name` ASC;