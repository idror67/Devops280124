select * from customers;
select customerName, addressLine1 from customers;

select distinct country from customers;

select * from employees;


select * from customers where country= 'USA';

select * from products order by buyPrice desc;



select * from products order by productLine desc;

select * from products order by productLine, buyPrice desc;

--  select all customers from USA order by contact first name 
select * from customers where country = 'USA' order by contactFirstName;


INSERT INTO Customers (CustomerNumber, CustomerName,contactFirstName, contactLastName, addressLine1, City, PostalCode, Country, phone) 
			   VALUES (497, 'Cardinal', 'Tom', 'B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway', '6175552555');

select * from customers where CustomerName = 'Cardinal';

update customers set contactlastname= 'shmidt' , contactfirstname='kurt', city = 'Frankfurt' where customernumber = 497;               

delete from customers where customerNumber = 497; 

update customers set phone = '' where customerNumber = 497; 

-- all customers in country mexico
select * from customers where country = 'MEXICO';

-- all customer in country germany and city berlin
select * from customers where country = 'germany' and city = 'berlin';


-- all customers ordered by country asc and by customername desc.
select * from customers order by country, customerName desc;

-- all customers where addressline1 is null
select * from customers where addressLine1 is null;

-- update all customers from spain with new name =>"juan"
update customers set contactFirstName = 'Juan' where country = 'spain';

-- to check that all customers from spain have name juan.
select * from customers where country = 'spain';

-- find the cheapest product using order by 
select * from products  order by buyPrice asc;

select buyPrice-5 from products;

select * from products where buyPrice > 50;

select * from customers where country <> 'usa';

select * from customers where state is not null;


select * from customers where city not in ('Las Vegas', 'NYC', 'San francisco');

select * from customers where country = 'usa' and  city != 'nyc';

select * from customers where country = 'usa' or   state is null ;

-- get products of types 'classic cars' or 'motorcycles' and id is bigger than 10 and lower than 35.
select * from products where productLine in ('classic cars', 'Motorcycles') and buyPrice between 11 and 35;
