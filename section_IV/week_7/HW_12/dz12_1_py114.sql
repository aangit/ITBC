
create database if not exists store1;
use store1;
create table if not exists buyer(
first_name varchar(100) not null,
last_name varchar(100) not null,
jmbg varchar(13) not null, 
tel varchar(100) not null,
place_name varchar(100) not null
)engine=InnoDB;

create table if not exists place(
name_place varchar(100) not null,
zip_code varchar(100) not null,
country varchar(100) not null
)engine=InnoDB;

create table if not exists material(
material_name varchar(100) not null,
material_description varchar(300) not null,
photo varchar(15) not null
)engine = InnoDB;

create table if not exists product(
product_name varchar(100) not null,
product_description varchar(100) not null,
photo varchar(100) not null,
price float not null
)engine = InnoDB;

create table if not exists components(
product_name varchar(100),
material_name varchar(100),
quantity int not null
)engine = InnoDB;

create table if not exists product_purchase(
product_name varchar(100) not null,
name_place varchar(100) not null,
buyer_name varchar(100) not null,
quantity int not null,
total_price int not null,
date_purchase date not null
)engine = InnoDB;

alter table buyer
add column id int primary key auto_increment;
alter table buyer
drop column place_name;

alter table place
add column id int primary key auto_increment;

alter table material
add column id int primary key auto_increment;

alter table product
add column id int primary key auto_increment;

alter table components
add column product_id int;

alter table components
add column material_id int;

alter table components

add foreign key (product_id) references product(id)
on update cascade on delete cascade,
add foreign key (material_id) references material(id)
on update cascade on delete cascade;

alter table components
drop column product_name;

alter table components
drop column material_name;

alter table product_purchase
add column product_name_id int;

alter table product_purchase
add column place_id int;

alter table product_purchase
add column buyer_id int;

alter table product_purchase
add foreign key (product_name_id) references product(id)
on update cascade on delete cascade,
add foreign key (place_id) references place(id)
on update cascade on delete cascade,
add foreign key (buyer_id) references buyer(id)
on update cascade on delete cascade;

alter table product_purchase
drop column product_name;

alter table product_purchase
drop column name_place;

alter table product_purchase
drop column buyer_name;

alter table buyer
add column place_id int;

alter table buyer
add foreign key (place_id) references place(id)
on update cascade on delete cascade;

alter table material
drop column photo;

alter table product
drop column photo;

alter table buyer
rename column tel to telephone;

create table if not exists delivery (
    id int primary key,
    customer_id int not null,
    place_id int not null,
    foreign key (customer_id) references buyer(id),
    foreign key (place_id) references place(id)
)engine=InnoDB;

insert into buyer (first_name, last_name, jmbg, telephone)
values ('Andjela', 'Dojcinovic', '1234567890', '0642424960');

insert into place (name_place, zip_code, country)
values ('Lebane', '16230' , 'Serbia');

insert into material (material_name, material_description)
values ('cashmere' , 'lux material, made from goats from China and Mongolia');

insert into product(product_name, product_description, price)
values ('scarf','long red scarf', 15.50);

insert into components (quantity)
values (52);

insert into product_purchase(quantity, total_price, date_purchase)
values (2 , 31 , '2022-01-10');

alter table product_purchase 
drop foreign key product_purchase_ibfk_3;

alter table buyer
drop foreign key buyer_ibfk_1;

alter table components
drop foreign key components_ibfk_1;

alter table components
drop foreign key components_ibfk_2;

alter table delivery
drop foreign key delivery_ibfk_1;

alter table delivery
drop foreign key delivery_ibfk_2;

alter table product_purchase
drop foreign key product_purchase_ibfk_1;

alter table product_purchase
drop foreign key product_purchase_ibfk_2;


delete from buyer;
delete from place;
delete from material;
delete from product;
delete from components;
delete from product_purchase;
delete from delivery;

drop table buyer;
drop table place;
drop table material;
drop table product;
drop table components;
drop table product_purchase;
drop table delivery;

drop database store1;