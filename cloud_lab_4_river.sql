DROP SCHEMA IF EXISTS cloud_lab_4;
create schema cloud_lab_4;
use cloud_lab_4;

CREATE TABLE IF NOT EXISTS river
(
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
sensor_id int not null UNIQUE,
name VARCHAR(45),
settlement VARCHAR(45),
latitude decimal(10,7),
longtitude decimal(10,7),
water_level float,
measurement_date timestamp
)
ENGINE = InnoDB;

INSERT INTO river (id, sensor_id, name, settlement, latitude, longtitude, water_level, measurement_date) VALUES 
(1, 1, 'river name', 'settlement name', 49.785537, 30.183090, 10.45, '2021-01-01 00:00:01'),
(2, 2, 'river name', 'settlement name', 49.785537, 30.183090, 10.45, '2021-01-01 00:00:01'),
(3, 3, 'river name', 'settlement name', 49.785537, 30.183090, 10.45, '2021-01-01 00:00:01')