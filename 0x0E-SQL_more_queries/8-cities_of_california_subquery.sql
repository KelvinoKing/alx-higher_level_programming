-- Lists all the cities of California that can be found in specified database
SELECT `id`, `name` FROM cities WHERE `state_id`=1
ORDER BY `id` ASC;
