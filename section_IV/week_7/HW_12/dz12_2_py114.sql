drop database if exists medical_records;
create database if not exists medical_records;
use medical_records;

create table if not exists patient(
first_name varchar(100) not null,
last_name varchar(100) not null,
jmbg varchar(13) not null, 
address varchar (100) not null,
telephone varchar(100) not null,
doctor_nr_licence varchar (100) not null
)engine = InnoDB;

create table if not exists doctor(
first_name varchar(100) not null,
last_name varchar(100) not null,
jmbg varchar(13) not null, 
specialization varchar(100) not null,
nr_licence varchar(100) not null
) engine = InnoDB;

create table if not exists medicine(
med_name varchar (100) not null,
med_code varchar (100) not null,
manufacturer_name varchar(100) not null
) engine = InnoDB;

create table if not exists illness(
illness_name varchar(100) not null,
illness_desc varchar(100) not null,
photo varchar(100)
) engine = InnoDB;

create table if not exists manufacturer(
manufacturer_name varchar(100) not null,
address varchar(100) not null,
tel varchar(100) not null
) engine = InnoDB;

create table if not exists suffers_from(
patient_name varchar(100) not null,
doctor_name varchar(100) not null,
illness_name varchar(100) not null,
diagnosed_on_date date not null
) engine = InnoDB;

alter table patient
add column id int primary key auto_increment;
alter table patient
drop column doctor_nr_licence;


alter table doctor
add column id int primary key auto_increment;

alter table medicine
add column id int primary key auto_increment;
alter table medicine
drop column manufacturer_name;

alter table medicine
add column manufacturer_id int;

alter table manufacturer
add column id int primary key auto_increment;

alter table illness
add column id int primary key auto_increment;

alter table suffers_from 
add column patient_id int;

alter table suffers_from
add column doctor_id int;

alter table suffers_from
add column illness_id int;

alter table patient
add column doctor_id int;

alter table patient
add foreign key (doctor_id) references doctor(id)
on update cascade on delete cascade;

alter table suffers_from
add foreign key (patient_id) references patient(id)
on update cascade on delete cascade,
add foreign key (doctor_id) references doctor(id)
on update cascade on delete cascade,
add foreign key (illness_id) references illness(id)
on update cascade on delete cascade;

alter table suffers_from
drop column patient_name;

alter table suffers_from
drop column doctor_name;

alter table suffers_from
drop column illness_name;

alter table medicine
add foreign key (manufacturer_id) references manufacturer(id)
on update cascade on delete cascade;

alter table illness
drop column photo;

alter table manufacturer
rename column tel to telephone;

create table if not exists doctor_cured(
id int primary key,
id_doctor int,
id_illness int,
foreign key (id_doctor) references doctor(id),
foreign key (id_illness) references illness(id)
)engine = InnoDB;

insert into doctor (first_name, last_name, jmbg, specialization, nr_licence) 
values ('Gavrilo' , 'Princip' , '123456789', 'pediatritian', '12345567');

insert into illness (illness_name, illness_desc)
values ('chickenpox', 'itchy, blister-like rash');

insert into manufacturer (manufacturer_name, address, telephone)
values ('Pfizer', '235 E 42nd St, New York, NY 10017, United States', '+1 212-733-2323');

insert into medicine (med_name, med_code)
values ('BioNTech', 'ZX998');

insert into patient (first_name, last_name, jmbg, address, telephone)
values ('Franc' , 'Ferdinand' , '98765432', 'Gratz', '06281914');

insert into suffers_from (diagnosed_on_date)
values ('1914-06-28');

alter table doctor_cured
drop foreign key doctor_cured_ibfk_1;

alter table doctor_cured
drop foreign key doctor_cured_ibfk_2;

alter table medicine
drop foreign key medicine_ibfk_1;

alter table patient
drop foreign key patient_ibfk_1;

alter table suffers_from
drop foreign key suffers_from_ibfk_1;

alter table suffers_from
drop foreign key suffers_from_ibfk_2;

alter table suffers_from
drop foreign key suffers_from_ibfk_3;

delete from doctor;
delete from doctor_cured;
delete from illness;
delete from manufacturer;
delete from medicine;
delete from patient;
delete from suffers_from;

drop table doctor;
drop table doctor_cured;
drop table illness;
drop table manufacturer;
drop table medicine;
drop table patient;
drop table suffers_from;

drop database medical_records;



