create database minichallenge;
create table my_contacts(
id int not null auto_increment,
C_Name varchar(20),
Phone varchar(50),
Email varchar(20),
Address varchar(100),
Primary Key(id)
);

select * from my_contacts;