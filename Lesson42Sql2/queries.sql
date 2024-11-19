-- HOMEWORK
-- Find all employees whose last names do not start with 'S'.
select * from employees;
select * from employees where lastName not like 's%';
-- SELECT * FROM employees WHERE lastName NOT REGEXP '^(p|m)';

-- Retrieve all products priced between $10 and $50, and whose names contain the word "dodge".
select * from products where productName like '%dodge%' and buyPrice between 10 and 50;

-- Get all customers who have a credit limit greater than $50000 and are located in either 'USA' or 'Canada'.
select * from customers where creditLimit > 50000 and country in ('usa', 'canada');

-- Retrieve all offices located in the 'United States' with a 'phone' number starting with the area code '212'.
select * from customers where country = 'USA' and phone like '212%';
select * from offices where country = 'USA' and phone like '%212%';

-- Get all order details for products with a price greater than $100.
select * from orderdetails where priceEach > 150;

-- MIN MAX COUNT SUM
select * from customers;
select * from products order by buyPrice;
select min(buyPrice) as minimumPrice from products;

select count(*) as number_Of_Products from products;

-- count number of products with price bigger than 20
select count(*) from products where buyPrice > 20;

select sum(quantityOrdered) from orderdetails;
select * from orderdetails;
select * from orderdetails where productCode like 'S18_2957';
select sum(priceEach * quantityOrdered) as total_paid_S18_2957 from orderdetails where productCode like 'S18_2957';

-- GROUP By
select * from customers;

select count(*),country from customers group by country order by count(*) asc;

-- list the maximum credit limit per country
-- max
select avg(creditLimit), city from customers group by city;

select * from orderdetails where orderNumber = 10100;
select * from products where productCode = 'S18_1749';
select * from orders where orderNumber = 10100;
select * from customers where customerNumber = 363;
select * from productlines where productLine = 'Vintage Cars';

-- inner join
select orders.orderNumber, orders.status, customers.contactLastName
  from orders join customers on orders.customerNumber = customers.customerNumber;

select avg(o.priceEach), p.productName, p.buyPrice from orderdetails o join products p on o.productCode = p.productCode
			group by p.productName, p.buyPrice;
            
-- Write query to get Customer Name and City, and office code  so we will see in the end all customers and the office codes related to each customer if exists the full match
-- We will not see any customer which doesnt have the same city as an office
-- We will not see any office which doesnt have at least one customer from the same city
select * from customers;
select * from offices;
-- join on ? city
-- what to show : Customer Name ? -> customers and City ? -> offices,customers , and office code ? -> offices

-- left join
select c.customerName, c.city, o.officeCode from customers c left join offices o on c.city = o.city;

-- right join            
select c.customerName, c.city,o.city, o.officeCode from customers c right join offices o on c.city = o.city;
                        

-- union operator
select city from offices 
union all
select city from customers;

select * from employees;

select officeCode, firstName from employees 
union 
select city, contactFirstName from customers;


select * from employees where lastName like 'p%'
union
select * from employees where lastName like 'm%';

-- exercises with joins
-- find all customers which have any order.
select o.orderNumber, c.customerNumber from orders o join customers c on o.customerNumber = c.customerNumber;

-- find all customers and their respecitve orders..
-- join? -> 
select o.orderNumber, c.customerNumber from orders o right join customers c on o.customerNumber = c.customerNumber;












