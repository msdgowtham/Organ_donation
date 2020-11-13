create database organdonation;

use organdonation;

create table users(email varchar(40) primary key, phone int(10), 
name varchar(30), pwd varchar(40),blood varchar(4),organ varchar(200))engine=InnoDB default charset=latin1;

