create database organdonation;

use organdonation;

create table users(donorid int primary key auto_increment,email varchar(40) unique, 
name varchar(30),age varchar(15), pwd varchar(40),blood varchar(4),heart int,liver int,
kidney int,eyes int,lungs int)engine=InnoDB default charset=latin1;

ALTER TABLE users AUTO_INCREMENT=100;

select * from users;


create table hospitals(id int primary key auto_increment,name varchar(30), Address varchar(70),
email varchar(40), pwd varchar(40))engine=InnoDB default charset=latin1;

ALTER TABLE hospitals AUTO_INCREMENT=100;

insert into hospitals values(null,"Apollo","Hyderabad","apollo@gmail.com",aes_encrypt("123",'passkey'));

select * from hospitals;