
-- creating views 

-- ----------------------------------------VIEWS FOR SALES SCHEMA -------------------------------------------------
USE sales;


CREATE OR REPLACE VIEW num_of_customers AS
	SELECT COUNT(*)
    FROM sales.customers;

CREATE OR REPLACE VIEW affiliated_stores AS
	SELECT store_name,store_id,city,state
    FROM (sales.stores) NATURAL JOIN (sales.location);

CREATE OR REPLACE VIEW working_states AS
	SELECT location.state
	FROM sales.location;
    
CREATE OR REPLACE VIEW staff_count AS
	SELECT COUNT(*)
    FROM sales.staffs;
    
CREATE OR REPLACE VIEW order_tally AS
	SELECT COUNT(*)
    FROM sales.order_items;
    
-- --------------------------------------SALES VIEWS END-----------------------------------------------------------------
    
-- ---------------------------VIEWS FOR PRODUCTION SCHEMA-----------------------------------------------------
USE production;

CREATE OR REPLACE VIEW num_of_availible_categories AS
	SELECT COUNT(*)
    FROM production.categories;
    
CREATE OR REPLACE VIEW display_brands AS
	SELECT *
    FROM production.brands;

CREATE OR REPLACE VIEW products_to_choose_from AS
	SELECT product_id,product_name,model_year,list_price
    FROM production.products;
    
CREATE OR REPLACE VIEW stock_info AS 
	SELECT product_name,product_id, quantity
    FROM production.stocks JOIN production.products
    USING (product_id);

-- -----------------------------------PRODUCTION VIEWS END ---------------------------------------------------------    
