/* write your SQL query below */

SELECT ReportsTo, COUNT(ReportsTo) AS Members, ROUND(AVG(Age), 0) AS 'Average Age'
FROM maintable_1VKV1 
WHERE ReportsTo IS NOT NULL
GROUP BY ReportsTo
