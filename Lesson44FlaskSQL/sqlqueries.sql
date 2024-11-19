-- The customers table should have columns for customer_id, name, address, 
--    phone, and any other relevant information about the customers.
-- The accounts table should have columns for account_id, customer_id, 
--   account_type, balance, and any other relevant information about the accounts.
-- The transactions table should have columns for transaction_id, account_id, 
--   amount, transaction_type, transaction_date, and any other relevant information about the transactions.

create database banking_system;
use banking_system;

create table customers (
	customer_id int primary key,
    name varchar(255),
    address varchar(255),
    phone varchar(255)
);

drop table customers;

create table accounts (
	account_id int primary key,
    customer_id int,
    account_type varchar(255),
    balance double
);

drop table accounts;



create table transactions (
	transaction_id int primary key,
    account_id int,
    transaction_type varchar(255),
    amount double,
    transaction_date date
);

drop table transactions;

-- adding foreign key to accounts table
ALTER TABLE accounts
ADD CONSTRAINT fk_customer21
FOREIGN KEY (customer_id) REFERENCES customers(customer_id);

-- adding foreign key to transactions table
alter table transactions
add constraint fk_transactions
foreign key (account_id) references accounts(account_id);



INSERT INTO customers (customer_id, name, address, phone) VALUES
(1, 'Alice Johnson', '123 Maple St, Springfield', '555-1234'),
(2, 'Bob Smith', '456 Oak St, Springfield', '555-5678'),
(3, 'Charlie Brown', '789 Pine St, Springfield', '555-9012');


INSERT INTO accounts (account_id, customer_id, account_type, balance) VALUES
(101, 1, 'Checking', 1500.00),
(102, 1, 'Savings', 3000.00),
(103, 2, 'Checking', 500.00),
(104, 3, 'Savings', 1200.00);


INSERT INTO transactions (transaction_id, account_id, amount, transaction_type, transaction_date) VALUES
(1001, 101, 200.00, 'Deposit', '2024-05-01'),
(1002, 101, -50.00, 'Withdrawal', '2024-05-02'),
(1003, 102, 300.00, 'Deposit', '2024-05-03'),
(1004, 103, -100.00, 'Withdrawal', '2024-05-04'),
(1005, 104, 200.00, 'Deposit', '2024-05-05'),
(1006, 101, -20.00, 'Withdrawal', '2024-05-06'),
(1007, 101, 100.00, 'Deposit', '2024-05-07'),
(1008, 102, -150.00, 'Withdrawal', '2024-05-08'),
(1009, 103, 300.00, 'Deposit', '2024-05-09'),
(1010, 104, -50.00, 'Withdrawal', '2024-05-10');


select * from transactions;

select * from customers;
select * from accounts where customer_id = 1;

delete from customers where customer_id = 1;

delete from accounts where account_id = 101;

delete from transactions where transaction_id = 1001;

select * from accounts;

update accounts set balance=2000 where account_id = 101;

select * from customers;
update customers set address='sheshet hayamim 29 rishon' where customer_id = 1;

-- Select all transactions of account where the balance > 1000
select t.*, a.balance from transactions t join accounts a on a.account_id = t.account_id where a.balance>1000;

-- Select phone number of contact of the account with the most transactions.
select c.phone from customers c 
				join accounts a on c.customer_id = a.customer_id 
                join transactions t on t.account_id = a.account_id where ;
-- targil etgar.                 
select count(account_id) , account_id from transactions group by account_id order by count(account_id) desc limit 1;


-- flights system ----------------------
CREATE TABLE countries (
Id INTEGER PRIMARY KEY AUTO_INCREMENT,
Name VARCHAR(255) NOT NULL
);

CREATE TABLE airlines (
Id INTEGER PRIMARY KEY AUTO_INCREMENT,
Name VARCHAR(255) NOT NULL,
Country_Id INTEGER NOT NULL
);

INSERT INTO countries (Id, Name) 
VALUES 
(1, 'Israel'),
(2, 'United States'),
(3, 'United Kingdom'),
(4, 'France'),
(5, 'United Arab Emirates');

INSERT INTO airlines (Id, Name, Country_Id) 
VALUES 
(1, 'El Al', 1),
(2, 'United Airlines', 2),
(3, 'British Airways', 3),
(4, 'Air France', 4),
(5, 'Emirates', 5);


select * from countries;

select * from countries where id = 1;


