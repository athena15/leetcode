-- https://leetcode.com/problems/customers-who-never-order/submissions/
-- Write your MySQL query statement below

SELECT Name as Customers
FROM Customers c
WHERE c.ID NOT IN (SELECT CustomerId FROM Orders)