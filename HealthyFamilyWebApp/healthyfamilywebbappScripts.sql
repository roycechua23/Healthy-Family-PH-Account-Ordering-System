Create Database healthy_family;

Use healthy_family;

CREATE TABLE `healthy_family`.`useraccount` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(45) UNIQUE NOT NULL,
  `user_username` VARCHAR(45) NOT NULL,
  `user_mobilenumber` VARCHAR(11) NOT NULL,
  `user_telephonenumber` VARCHAR(11) NOT NULL,
  `user_emailaddress` VARCHAR(45) NULL,
  `user_address` VARCHAR(100) NOT NULL,
  `user_password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`user_id`));

#DROP TABLE useraccount;
ALTER TABLE useraccount
MODIFY user_username VARCHAR(45) UNIQUE NOT NULL;

ALTER TABLE useraccount MODIFY user_password VARCHAR(100) NOT NULL;

#DROP PROCEDURE usp_createUser;
DELIMITER //
CREATE PROCEDURE usp_createUser(
	IN name VARCHAR(45),
	IN username VARCHAR(45),
    IN mobilenumber VARCHAR(11),
    IN telephonenumber VARCHAR(11),
    IN emailaddress VARCHAR(45),
    IN address VARCHAR(100),
    IN password VARCHAR(100)
)
BEGIN
	if ( SELECT EXISTS ( SELECT 1 FROM useraccount WHERE user_name = name AND user_username=username) ) THEN
    SELECT 'User already exists';
    else
		INSERT INTO useraccount (user_name,user_username,user_mobilenumber,user_telephonenumber,user_emailaddress,user_address,user_password)
        VALUES (name,username,mobilenumber,telephonenumber,emailaddress,address,password);
	END IF;
END //
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE usp_verifyUser(
	IN username VARCHAR(45)
)
BEGIN
	SELECT user_password,user_name FROM useraccount WHERE user_username = username;
END $$
DELIMITER ;

CREATE TABLE IF NOT EXISTS `healthy_family`.`userorder` (
  `order_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT(11) NOT NULL,
  `order_quantity` INT NOT NULL,
  `order_date` TIMESTAMP NOT NULL,
  `order_transactionstatus` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`order_id`),
  INDEX `fk_table1_useraccount_idx` (`user_id` ASC),
  CONSTRAINT `fk_table1_useraccount`
    FOREIGN KEY (`user_id`)
    REFERENCES `healthy_family`.`useraccount` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB

DELIMITER //
CREATE PROCEDURE usp_showOrders(
    IN username varchar(45)
)
BEGIN
	#DECLARE id int;
    #SET id = (SELECT user_id FROM useraccount where user_username=username);
    
	SELECT order_id,order_quantity,order_date,order_transactionstatus FROM userorder;
    
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE usp_createOrder(
    IN username varchar(45),
    IN qty int
)
BEGIN
	DECLARE id int;
    SET id = (SELECT user_id FROM useraccount where user_username=username);
    
	INSERT INTO userorder (user_id,order_quantity,order_date,order_transactionstatus)
    VALUES (id,qty,CURRENT_TIMESTAMP,'Pending');
END //
DELIMITER ;


