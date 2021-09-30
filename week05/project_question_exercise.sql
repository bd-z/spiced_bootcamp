

    -- Get the names and the quantities in stock for each product.

    -- Get a list of current products (Product ID and name).

    -- Get a list of the most and least expensive products (name and unit price).

    -- Get products that cost less than $20.

    -- Get products that cost between $15 and $25.

    -- Get products above average price.

    -- Find the ten most expensive products.

    -- Get a list of discontinued products (Product ID and name).

    -- Count current and discontinued products.

    -- Find products with less units in stock than the quantity on order.

    -- Find the customer who had the highest order amount

    -- Get orders for a given employee and the according customer

    -- Find the hiring age of each employee

    -- Create views and/or named queries for some of these queries






select productID,productName,unitsInStock FROM products;
select productID,productName,unitsInStock FROM products;
select productName, unitPrice FROM products WHERE unitPrice = ( SELECT MAX(unitPrice) FROM products) or unitPrice =( SELECT MIN(unitPrice) from products);
select productName, unitPrice FROM products WHERE unitPrice < 20 ;
select productName, unitPrice FROM products WHERE unitPrice < 25 AND unitPrice > 15;
SELECT productName, unitPrice FROM products WHERE unitPrice > (SELECT AVG(unitPrice) FROM products);
SELECT productName, productID FROM products WHERE discontinued = 1;
SELECT count (productName) from products WHERE discontinued=1 and unitsInStock > 0;
SELECT productName, unitsInStock, quantity from products inner join order_details on order_details.productID = order_details.productID
WHERE products.unitsInStock < order_details.quantity;
SELECT distinct customerID, quantity from orders inner join order_details on orders.orderID =
order_details.orderID order by quantity desc limit 1;

SELECT orders.employeeID,employees.lastName, employees.firstName, orders.orderID, 
order_details.quantity FROM 
(orders left join order_details on orders.orderID = order_details.orderID) 
left join employees on orders.employeeID=employees.employeeID
WHERE orders.employeeID = 5;

#doesn't work : select employeeID, to_number(to_char( (hireDate - birthDate)/365)) as Age from employees;
select employeeID, (hireDate - birthDate)/365 as Age from employees;

CREATE VIEW myview AS 
SELECT distinct customerID, quantity from orders inner join order_details on orders.orderID =
order_details.orderID order by quantity desc limit 5;
