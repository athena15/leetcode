--    https://leetcode.com/problems/duplicate-emails/


--    Write a SQL query to find all duplicate emails in a table named Person.
--
--    +----+---------+
--    | Id | Email   |
--    +----+---------+
--    | 1  | a@b.com |
--    | 2  | c@d.com |
--    | 3  | a@b.com |
--    +----+---------+

-- Write your MySQL query statement below

SELECT DISTINCT p1.Email
FROM Person p1, Person p2
WHERE p1.Email = p2.Email AND p1.Id <> p2.Id

-- OR

SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(Email) > 1