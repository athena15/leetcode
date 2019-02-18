--    https://leetcode.com/problems/consecutive-numbers/

--    Write a SQL query to find all numbers that appear at least three times consecutively.
--
--    +----+-----+
--    | Id | Num |
--    +----+-----+
--    | 1  |  1  |
--    | 2  |  1  |
--    | 3  |  1  |
--    | 4  |  2  |
--    | 5  |  1  |
--    | 6  |  2  |
--    | 7  |  2  |
--    +----+-----+
--
--    For example, given the above Logs table, 1 is the only number that appears consecutively for at least three times.
--
--    +-----------------+
--    | ConsecutiveNums |
--    +-----------------+
--    | 1               |
--    +-----------------+

SELECT DISTINCT L1.Num AS ConsecutiveNums
FROM Logs L1, Logs L2, Logs L3
WHERE L1.Id + 1 = L2.Id
AND L2.Id + 1 = L3.Id
AND L1.Num = L2.Num
AND L2.Num = L3.Num