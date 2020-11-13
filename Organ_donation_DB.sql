create database organdonation;

use organdonation;

create table users(donorid int primary key auto_increment,email varchar(40) unique, 
name varchar(30),age varchar(15), pwd varchar(40),blood varchar(4),heart int,liver int,
kidney int,eyes int,lungs int)engine=InnoDB default charset=latin1;

ALTER TABLE users AUTO_INCREMENT=100;

select * from users;

