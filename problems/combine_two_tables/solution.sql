# Write your MySQL query statement below
SELECT
p.FirstName, p.LastName, a.city, a.state
from
Person P
left join
      Address a on p.PersonID = a. PersonID;