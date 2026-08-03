# Write your MySQL query statement below
SELECT * FROM CINEMA
WHERE id % 2 = 1 and DESCRIPTION != 'boring'
order by rating DESC;