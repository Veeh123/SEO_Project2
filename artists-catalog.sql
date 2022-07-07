CREATE DATABASE IF NOT EXISTS artist_hits;

CREATE TABLE catalog ( 
    id INT(8) UNSIGNED NOT NULL auto_increment,
    name VARCHAR(255) default NULL,
    manufacture_year YEAR(4) default NULL,
    brand VARCHAR(255) default NULL,
    PRIMARY KEY (id)
) AUTO_INCREMENT=1;