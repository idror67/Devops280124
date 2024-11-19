-- List all customers with their corresponding sales representative's first and last name:
select * from employees;
select * from customers;
select customers.customerName, employees.firstName, employees.lastName from customers 
left join employees on employees.employeeNumber = customers.salesRepEmployeeNumber;

-- Find the product lines with their respective product count:
select * from productlines;
select * from products;
select productLine, count(productline) from products group by productLine;

-- List all orders along with the customer name and order status:
select * from orders;
select c.customerName, o.* from orders o left join customers c on c.customerNumber = o.customerNumber;

-- Retrieve the product details along with their product line information:
select * from products;
select * from productlines;
select * from products pr join productlines pl on pl.productLine = pr.productLine; 

-- Get the employees who have reported to another employee (i.e., have a manager):
select * from employees where reportsTo is not null;

-- Find the average credit limit for customers in each country:
select * from customers order by country;
select AVG(creditLimit), country from customers group by country;

-- Calculate the total quantity in stock for each product line:
select sum(quantityInStock), productLine from products group by productLine;

-- NEW LESSON -- DATABASE SCHEMA MANIPULATIONS
-- create dbs
show databases;
create database my_db;
create schema my_db1;
use my_db;
show tables;
-- create tables
CREATE TABLE person (
    firstname varchar(255),
    lastname varchar(255),
    age int  
);
select * from person;

-- EXERCISE ...
-- Create database Lesson3
-- Use that database (use lesson3)
-- Create Table Actors. With columns First name Last name , Age , and Favorite movie
-- Insert few lines to that table :
-- insert example
INSERT INTO Actors (first_name, last_name, age, favorite_movie)
VALUES 
    ('Tom', 'Hanks', 65, 'Forrest Gump');

create schema lesson3;
use lesson3;
CREATE TABLE Actors (
    firstname varchar(255),
    lastname varchar(255),
    age int,  
    Favoritemovie varchar(255)
);
INSERT INTO Actors (firstname, lastname, age, Favoritemovie)
VALUES 
    ('Tom', 'Hanks', 65, 'Forrest Gump'),
    ('Richard', 'Gere', 60, 'Pretty Women'),
    ('Christian', 'Bale', 47, 'Batman Dark Knight'),
    ('Liam', 'Neesan', 68, 'Taken');

select * from actors;

-- exercise together:
-- add column to actors with name gender and type varchar(1)
ALTER TABLE actors ADD gender varchar(1);
update actors set gender='m' where 1=1; 

alter table actors drop gender;

truncate table actors;
drop table actors;
drop database lesson3;


select * from customers;
select * from products;
select * from orderdetails;
select * from orders;



CREATE TABLE Persons (
	ID int NOT NULL,
    LastName varchar(255) NOT NULL,
	FirstName varchar(255) NOT NULL,
	Age int
);
select * from persons;
INSERT INTO persons (ID, lastname, FirstName, Age)
VALUES 
    (123, 'Hanks', 'tom', 15);
INSERT INTO persons (ID, lastname, FirstName, Age)
VALUES 
    (1223, 'Travolta', 'tom', null);
    
    
CREATE TABLE courses (
  course_id INT NOT NULL ,
  course_name VARCHAR(50) NOT NULL,
  instructor_name VARCHAR(50) NOT NULL,
  course_description TEXT NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  PRIMARY KEY (course_id)
);
    

INSERT INTO courses (course_id ,course_name, instructor_name, course_description, start_date, end_date)
VALUES 
(1, 'Intro to Python', 'John Smith', 'Learn the basics of Python programming', '2023-05-01', '2023-06-01'),
(2, 'Web Development', 'Sarah Johnson', 'Learn how to build dynamic websites with HTML, CSS, and JavaScript', '2023-06-15', '2023-08-15'),
(3, 'Data Analysis with R', 'David Lee', 'Analyze and visualize data using the R programming language', '2023-07-01', '2023-08-01');


select * from courses;


CREATE TABLE students (
  student_id INT NOT NULL,
  student_name VARCHAR(50) NOT NULL,
  course_id INT,
  PRIMARY KEY (student_id),
  FOREIGN KEY (course_id) REFERENCES courses(course_id)
);


INSERT INTO students (student_id, student_name, course_id)
VALUES 
  (1, 'Jane Doe', 1),  (2, 'John Smith', 2),  (3, 'Sarah Johnson', 3),  (4, 'David Lee', 1),
  (5, 'Emily Brown', 2),  (6, 'Michael Chen', null),  (7, 'Julia Kim', 1),  (8, 'Alex Wong', 2),
  (9, 'Elena Rodriguez', 3),  (10, 'Chris Patel', 1);

select * from students;
delete from courses where course_id = 3;

