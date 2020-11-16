create database organdonation;

use organdonation;

create table blood_group (blood varchar(5) primary key);

insert into blood_group values("A+"),("B+"),("AB+"),("O+"),("A-"),("B-"),("AB-"),("O-");

create table users(donorid int primary key auto_increment,email varchar(40) unique, 
name varchar(30),age varchar(15), pwd varchar(40),blood varchar(5),heart int,liver int,
kidney int,eyes int,lungs int,blood_donation boolean,city varchar(20),phone varchar(10))engine=InnoDB default charset=latin1;

ALTER TABLE users AUTO_INCREMENT=100;

select * from users;
select * from users where blood_donation=1 and blood="B+" and city like "%vij%";


create table hospitals(id int primary key auto_increment,name varchar(30), Address varchar(70), phone varchar(15),
email varchar(40), pwd varchar(40))engine=InnoDB default charset=latin1;

ALTER TABLE hospitals AUTO_INCREMENT=100;

insert into hospitals values(null,"Apollo","Hyderabad","0402534562","apollo@gmail.com",aes_encrypt("123",'passkey'));
insert into hospitals values(null,"Kims","Hyderabad, LB Nagar","0402334562","apollo@gmail.com",aes_encrypt("123",'passkey'));
insert into hospitals values(null,"Ramesh","Vijayawada","08662534162","apollo@gmail.com",aes_encrypt("123",'passkey'));
insert into hospitals values(null,"Ayush","Amaravati","08662534562","apollo@gmail.com",aes_encrypt("123",'passkey'));

select * from hospitals;

select * from hospitals where Address like "%hyd%";

drop table users;