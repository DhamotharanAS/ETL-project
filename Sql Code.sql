create database Shops;
use Shop;

CREATE TABLE Customer (
CustomerID INT PRIMARY KEY,
FirstName VARCHAR(50),
LastName VARCHAR(50),
Address VARCHAR(255)
);

 

 

CREATE TABLE Orders (
OrderID INT PRIMARY KEY,
CustomerID INT,
Year_month_date varchar(30),
FOREIGN KEY (CustomerID) REFERENCES Customer (CustomerID)
);

 

 

CREATE TABLE Product (
ProductID INT PRIMARY KEY,
Name VARCHAR(100),
Description VARCHAR(255),
Price int);

 

 

CREATE TABLE OrderItem (
OrderItemID INT primary key,
OrderID INT,
ProductID INT,
Quantity INT,
FOREIGN KEY (OrderID) REFERENCES Orders (OrderID),
FOREIGN KEY (ProductID) REFERENCES Product (ProductID)
);

 

 

 




 


INSERT INTO Customer (CustomerID, FirstName, LastName, Address)
VALUES
(1, 'Dhamo', 'tharan', '27 Periyar nagar ,Chennai-600044'),
(2, 'Rahul', 'S', '456 Elm St,Chennai-600053'),
(3, 'Praveen', 'G', '789 Oak St,Chennai-600040'),
(4, 'Vishwa', 'R', '321 Pine St,Chennai-600059'),
(5, 'Likitha', 'C H', '654 Maple St,chennai-600032'),
(6, 'Dharshini', 'M', '987 Oak Ave,chennai-600031'),
(7, 'Vasavi', 'Manam', '654 Elm Ave,chennai-600039'),
(8, 'Ganesh', 'Gopi', '321 Pine Ave,chennai-600045'),
(9, 'Naveen','Kumar', '789 Maple Ave,chennai-600050'),
(10, 'Abinaya', 'A', '123 Oak Blvd,chennai-600060');

 

 

INSERT INTO Orders (OrderID, CustomerID, Year_month_date)
VALUES
(1, 1, '2023-05-01'),
(2, 2, '2023-05-03'),
(3, 3, '2023-05-05'),
(4, 4, '2023-05-07'),
(5, 5, '2023-05-09'),
(6, 6, '2023-05-11'),
(7, 7, '2023-05-13'),
(8, 8, '2023-05-15'),
(9, 9, '2023-05-17'),
(10, 10, '2023-05-19');

 

 

INSERT INTO Product (ProductID, Name, Description,Price)
VALUES
(1, 'Espresso', 'Strong and concentrated coffee',10),
(2, 'Cappuccino', 'Espresso with steamed milk and foam',12),
(3, 'Latte', 'Espresso with steamed milk',14),
(4, 'Mocha', 'Espresso with chocolate and steamed milk',11),
(5, 'Americano', 'Espresso with hot water',09),
(6, 'Green Tea', 'Light and refreshing tea',08),
(7, 'Black Tea', 'Strong and bold tea',20),
(8, 'Chamomile Tea', 'Herbal tea for relaxation',15),
(9, 'Earl Grey', 'Tea with a hint of bergamot flavor',13),
(10, 'Peppermint Tea', 'Cooling and soothing herbal tea',16);

 

 

INSERT INTO OrderItem (OrderItemID, OrderID, ProductID, Quantity)
VALUES
(1, 1, 1, 2),
(2, 1, 6, 1),
(3, 2, 3, 1),
(4, 3, 9, 2),
(5, 4, 2, 3),
(6, 5, 4, 1),
(7, 6, 7, 2),
(8, 7, 10, 1),
(9, 8, 5, 2),
(10, 9, 8, 1);

 

select * from OrderItem;
select * from Product;
select * from Orders;
select * from Customer;
create database target_database;
use target_database;
show tables;

 

create table OrderItem_Orders(OrderID varchar(255),OrderItemID varchar(255),
CustomerID varchar(255),ProductID varchar(255),Quantity varchar(255),Date_month_year varchar(255));
create table OrderItem_Product(ProductID varchar(255),OrderItemID varchar(255),OrderID varchar(255),Name varchar(255),
Description varchar(255),Price varchar(255),Quantity varchar(255));

 


create table Orders_Customer(CustomerID varchar(255),OrderID varchar(255),
FullName varchar(255),street varchar(255),city_Pin_Code varchar(255),Date_month_year varchar(255));

 

select * from OrderItem_Orders;
select * from OrderItem_Product;
select * from Orders_Customer;