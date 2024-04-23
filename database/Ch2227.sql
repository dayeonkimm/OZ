USE classicmodels;

# 1. 생성(CREATE)
-- INSERT INTO customers (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, creditLimit)
-- VALUES (777, 'pyo', 'Hong', 'James', 50243453, 'cheongwa', '153gil', 'seoul', 'mapogu', 30000); 
-- INSERT INTO orders (orderNumber, orderDate, requiredDate, shippedDate, status, customerNumber)
-- VALUES (10426, '2005-06-02', '2005-06-08', '2005-06-04', 'Shipped', 777);
-- INSERT INTO orderdetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber)
-- VALUES (10426, 'S700_3505', 40, 92.16, 6);

-- INSERT INTO employees (employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle)
-- VALUES (1819, 'kim', 'John', 'x9273', 'Jokim@gmail.com', 4, 1102, 'Sales Rep');
-- UPDATE employees AS e1
-- JOIN employees AS e2 ON e1.lastName = 'kim' AND e2.jobTitle = 'Sales Manager (APAC)'
-- SET e1.reportsTo =  e2.employeeNumber; 

-- INSERT INTO products (productCode,productName,productLine,productScale,productVendor,productDescription,quantityInStock,buyPrice,MSRP)
-- VALUES ('S10_1679','1974 Harley Davidson Ultimate Cycle','Motorcycles','1:50','Min Lin Diecast','This replica features working kickstand, front suspension, gear-shift lever, footbrake lever, drive chain, wheels and steering. All parts are particularly delicate due to their precise scale and require special care and attention.',428,'50.16','95.70');
-- INSERT INTO orders (orderNumber,orderDate,requiredDate,shippedDate,status,comments,customerNumber) 
-- VALUES (10427,'2005-06-12','2005-06-18','2005-06-15','Shipped',NULL,363);
-- INSERT INTO orderdetails (orderNumber,productCode, quantityOrdered, priceEach, orderLineNumber)
-- VALUES (10427,'S10_1679', 42, 70.15, 15);

-- INSERT INTO orders (orderNumber,orderDate,requiredDate,shippedDate,status,comments,customerNumber) 
-- VALUES (10428,'2005-06-13','2005-06-15',NULL,'In Process',NULL,777);
-- INSERT INTO payments (customerNumber,checkNumber,paymentDate,amount) 
-- VALUES (777,'HP930428','2005-06-13','5061.88');

-- INSERT INTO orderdetails (orderNumber,productCode, quantityOrdered, priceEach, orderLineNumber)
-- VALUES (10428,'S24_1046', 85, 70.05, 15);
-- UPDATE products
-- SET quantityInStock = quantityInStock-85 WHERE productCode='S24_1046'; 

# 2. 읽기 (READ)
-- SELECT city, COUNT(*) AS NumOfCustomers FROM customers GROUP BY city;
-- SELECT productLine, AVG(buyPrice) AS avgPrice FROM products GROUP BY productLine;
-- SELECT officeCode, COUNT(*) AS NumOfEmployees FROM employees GROUP BY officeCode;
-- SELECT productCode, SUM(quantityOrdered) AS Sum FROM orderdetails GROUP BY productCode LIMIT 5;

# 3. 갱신 (UPDATE)
-- UPDATE orders
-- SET status='On Hold' WHERE orderDate BETWEEN '2004-01-01' AND '2004-12-31';
-- UPDATE orderdetails
-- SET priceEach = priceEach*1.3 WHERE productCode='S24_2300';
-- UPDATE payments
-- SET paymentDate = '2005-06-01' WHERE paymentDate BETWEEN '2005-05-01' AND '2005-05-31';
-- UPDATE productlines
-- SET textDescription='New updated description' WHERE productLine IN (SELECT productLine FROM products WHERE quantityInStock < 10);
-- UPDATE customers
-- SET addressLine1 = 'New Address', addressLine2 = NULL WHERE customerNumber BETWEEN 100 AND 130;

# 4. 삭제 (DELETE)
-- DELETE FROM orders WHERE orderDate BETWEEN '2005-01-01' AND '2005-12-31';
-- DELETE FROM orderdetails 
-- WHERE productCode =(
-- 	SELECT productCode 
--     FROM (
-- 		SELECT productCode, SUM(quantityOrdered) AS sumOf 
-- 		FROM orderdetails 
-- 		GROUP BY ProductCode 
-- 		ORDER BY sumOf ASC 
-- 		LIMIT 1
--     )AS min_order);
-- DELETE FROM payments WHERE amount<100;
-- DELETE FROM productlines WHERE productLine NOT IN (SELECT productLine FROM products); 
-- DELETE FROM customers WHERE customerNumber NOT IN (SELECT customerNumber FROM orders o WHERE o.orderDate BETWEEN '2005-01-01' AND '2005-12-31'); 
