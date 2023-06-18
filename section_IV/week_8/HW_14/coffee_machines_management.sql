-- drop database coffee_machine_management;
create database coffee_machine_management;
use coffee_machine_management;

CREATE TABLE IF NOT EXISTS coffee_machine (
	coffee_machine_id INT AUTO_INCREMENT PRIMARY KEY,
    serial_number VARCHAR(20) NOT NULL UNIQUE,
	installation_address VARCHAR(100) NOT NULL,
    installation_date DATE NOT NULL,
    operational_status INT,
    error_code VARCHAR(100),
    device_model_id INT, -- **
    resources_level_id INT -- **
);

CREATE TABLE IF NOT EXISTS device_model (
	device_model_id INT AUTO_INCREMENT PRIMARY KEY,
    model_name VARCHAR(30) NOT NULL,
    model_number VARCHAR(15) NOT NULL,
    water_capacity_liters float,
    coffee_capacity_kgs float,
    milk_capacity_kgs float,
    sugar_capacity_kgs float,
    sweetener_capacity_count INT,
    cups_capacity_count INT
);

CREATE TABLE IF NOT EXISTS resources_level (
	resources_level_id INT AUTO_INCREMENT PRIMARY KEY,
    water_level_liters float,
    coffee_level_kgs float,
    milk_level_kgs float,
    sugar_level_kgs float,
    sweetener_level_count INT,
    cups_level_count INT,
    coffee_machine_id INT NOT NULL -- **
);

CREATE TABLE IF NOT EXISTS beverage (
	beverage_id INT AUTO_INCREMENT PRIMARY KEY,
    beverage_name VARCHAR(20),
    price float,
    water_quantity_milliliters INT,
    milk_quantity_grams INT,
    cofee_quantity_grams INT
);

CREATE TABLE IF NOT EXISTS device_model_produces_beverage (
	device_model_id INT, -- **
    beverage_id INT -- **
);

CREATE TABLE IF NOT EXISTS maintenance_action (
	maintenance_action_id INT AUTO_INCREMENT PRIMARY KEY,
    action_datetime DATETIME NOT NULL,
    maintenance_action_type INT NOT NULL,
	coffee_machine_id INT -- **
);

-- There are 3 possible values for activity (ON, OFF, ERROR) - write check ******

alter table coffee_machine
add constraint chk_status check (operational_status in (1, 2, 3));



-- There are 7 possible values for maintenance type
-- (WATER_REFILL, COFFEE_REFILL, CUPS_REFILL, SUGAR_REFILL, MILK_REFILL, SWEETENER_REFILL, MISC_ERROR_REPAIR) - write check*****

alter table maintenance_action
add constraint chk_maint_action_type check (maintenance_action_type < 8 and maintenance_action_type > 0);


 
-- write all foreign key constraints. Noted by ** above

alter table coffee_machine
add constraint fk_device_model_id foreign key (device_model_id) references device_model(device_model_id);

alter table coffee_machine
add constraint fk_resources_level_id foreign key (resources_level_id) references resources_level(resources_level_id);

alter table resources_level
add constraint fk_coffee_machine_id foreign key (coffee_machine_id) references coffee_machine(coffee_machine_id);

alter table device_model_produces_beverage
add constraint fk_device_model_id_1 foreign key (device_model_id) references device_model(device_model_id);

alter table device_model_produces_beverage
add constraint fk_beverage_id foreign key (beverage_id) references beverage(beverage_id);

alter table maintenance_action
add constraint fk_coffee_machine_id_1 foreign key (coffee_machine_id) references coffee_machine(coffee_machine_id);



INSERT INTO device_model VALUES (NULL, 'Dolce Gusto Grande','NSKDJ556/4', 13.5, 5, 4, 7, 1200, 600);
INSERT INTO device_model VALUES (NULL, 'Phillips C series','skdjnfjee',  15, 7, 6, 9, 1500, 800);
INSERT INTO device_model VALUES (NULL, 'De Longhi ','ddtkkmnxsa-66', 7.5, 4, 2, 4, 400, 400);

INSERT INTO coffee_machine VALUES (NULL, '3452345-AK', 'Obrenovićeva 45a, 18000 Niš', '2023-01-13', 1, NULL, 1, NULL);
INSERT INTO coffee_machine VALUES (NULL, '2132133-BY', 'Učitelj Tasina 21, 18000 Niš', '2023-01-09', 1, NULL, 1, NULL);
INSERT INTO coffee_machine VALUES (NULL, '2343245-NM', 'Tome Rosandića 5, 18000 Niš', '2022-06-09', 1, NULL, 2, NULL);
INSERT INTO coffee_machine VALUES (NULL, '4565434-DU', 'Trg Kralja Milana 2, 18000 Niš', '2023-05-13',1, NULL, 1, NULL);

INSERT INTO resources_level VALUES (NULL, 5, 3.5, 0.4, 1.2, 200, 3, 1);
INSERT INTO resources_level VALUES (NULL, 4, 2.5, 0.5, 2.2, 140, 79, 2);
INSERT INTO resources_level VALUES (NULL, 6, 3.7, 0.9, 2.05, 174, 67, 3);
INSERT INTO resources_level VALUES (NULL, 4.3, 1.5, 1.5, 2.24, 50, 56, 4);

UPDATE coffee_machine SET resources_level_id = 1 where coffee_machine_id = 1;
UPDATE coffee_machine SET resources_level_id = 2 where coffee_machine_id = 2;
UPDATE coffee_machine SET resources_level_id = 3 where coffee_machine_id = 3;
UPDATE coffee_machine SET resources_level_id = 4 where coffee_machine_id = 4;

INSERT INTO beverage VALUES (NULL, 'Cappuccino', 160, 200, 30, 8);
INSERT INTO beverage VALUES (NULL, 'Espresso', 130, 30, 0, 7);
INSERT INTO beverage VALUES (NULL, 'Macchiato', 150, 60, 7, 8);
INSERT INTO beverage VALUES (NULL, 'Caffe Latte', 170, 220, 50, 9);

INSERT INTO device_model_produces_beverage VALUES (1, 1);
INSERT INTO device_model_produces_beverage VALUES (1, 2);
INSERT INTO device_model_produces_beverage VALUES (1, 3);
INSERT INTO device_model_produces_beverage VALUES (1, 4);

INSERT INTO device_model_produces_beverage VALUES (2, 1);
INSERT INTO device_model_produces_beverage VALUES (2, 2);
INSERT INTO device_model_produces_beverage VALUES (2, 4);

INSERT INTO device_model_produces_beverage VALUES (3, 1);
INSERT INTO device_model_produces_beverage VALUES (3, 2);
