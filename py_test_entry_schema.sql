-- CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
CREATE USER IF NOT EXISTS USCGuser@localhost IDENTIFIED BY 'USCG123';

DROP DATABASE IF EXISTS datalogDB2; 
SET default_storage_engine=InnoDB;
SET NAMES utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE DATABASE IF NOT EXISTS datalogDB2
    DEFAULT CHARACTER SET utf8mb4 
    DEFAULT COLLATE utf8mb4_unicode_ci;

--GRANT SELECT, INSERT, UPDATE, DELETE, FILE ON *.* TO 'USCGuser'@'localhost';
--GRANT ALL PRIVILEGES ON `USCGuser`.* TO 'USCGuser'@'localhost';
--GRANT ALL PRIVILEGES ON `datalogDB`.* TO 'USCGuser'@'localhost';
--FLUSH PRIVILEGES;





CREATE TABLE datalogDB2.data (
	EID INT NOT NULL AUTO_INCREMENT,
	
	value0 FLOAT,
	PRIMARY KEY (EID)
	);	
--DT DATETIME,