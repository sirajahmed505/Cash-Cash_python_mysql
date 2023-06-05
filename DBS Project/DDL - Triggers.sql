CREATE SCHEMA SalesProductionAudit;

USE SalesProductionAudit;

CREATE TABLE ProductAudit (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    product_name VARCHAR(50) NOT NULL,
    changedat DATETIME DEFAULT NULL,
    action VARCHAR(50) DEFAULT NULL
);

CREATE TABLE OrderAudit (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    customer_id INT NOT NULL,
    changedat DATETIME DEFAULT NULL,
    action VARCHAR(50) DEFAULT NULL
);

CREATE TABLE OrderItemsAudit (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    item_id INT NOT NULL,
    changedat DATETIME DEFAULT NULL,
    action VARCHAR(50) DEFAULT NULL
);

-- ----------------------------TRIGGER FOR SALES--------------------------

USE sales; 

CREATE TABLE CustomerAudit (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    changedat DATETIME DEFAULT NULL,
    action VARCHAR(50) DEFAULT NULL
);

CREATE TRIGGER before_customer_update 
    BEFORE UPDATE ON sales.customerS
    FOR EACH ROW 
 INSERT INTO SalesProductionAudit.CustomerAudit
 SET action = 'update',
     customer_id = OLD.customer_id,
     last_name = OLD.last_name,
     changedat = NOW();

CREATE TRIGGER before_order_update 
    BEFORE UPDATE ON sales.orders
    FOR EACH ROW 
 INSERT INTO SalesProductionAudit.OrderAudit
 SET action = 'update',
     order_id = OLD.order_id,
     customer_id = OLD.customer_id,
     changedat = NOW();
     
CREATE TRIGGER before_order_update 
    BEFORE UPDATE ON sales.order_items
    FOR EACH ROW 
 INSERT INTO SalesProductionAudit.OrderItemsAudit
 SET action = 'update',
     order_id = OLD.order_id,
     item_id = OLD.item_id,
     changedat = NOW();


-- ---------------TRIGGERS FOR PRODUCTION -----------------------------------

USE production;

CREATE TRIGGER before_order_update 
    BEFORE UPDATE ON production.products
    FOR EACH ROW 
 INSERT INTO SalesProductionAudit.ProductAudit
 SET action = 'update',
     product_id = OLD.product_id,
     product_name = OLD.product_name,
     changedat = NOW();
