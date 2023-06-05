-- STORED PROCEEDURES FOR SALES SCHEMA
USE sales;

-- procedure to display the customers list from the entered city
DELIMITER //
CREATE PROCEDURE SelectCustomerFromACity(input_city varchar(20))
BEGIN
	SELECT * 
	FROM (sales.customers NATURAL JOIN sales.location)
	WHERE city = input_city ;
END //

DELIMITER //
CREATE PROCEDURE zipcodeToLocation(in_zipcode varchar(20))
BEGIN
	SELECT city,states
	FROM (sales.customers NATURAL JOIN sales.location)
	WHERE zipcode = in_zipcode ;
END //

DELIMITER //
CREATE PROCEDURE customerLoginVerification(cust_id INT,cust_pass varchar(20))
BEGIN
	SELECT customer_id 
	FROM login_info
	WHERE login_info.customer_id = cust_id & login_info.customer_password = cust_pass ;
END //

DELIMITER //
CREATE PROCEDURE adminLoginVerification(mang_id INT,mang_pass varchar(20))
BEGIN
	SELECT store_manager_id 
	FROM admin_login
	WHERE admin_login.store_manager_id = mang_id & admin_login.manager_password = mang_pass ;
END //

-- STORED PRECEEDURES FOR PRODUCTION SCHEMA
USE production;

DELIMITER //
CREATE PROCEDURE stocksView()
BEGIN
	SELECT *
	FROM production.stocks;
END //