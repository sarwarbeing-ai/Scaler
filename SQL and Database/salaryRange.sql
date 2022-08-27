/*Find those employee's full_name (first name and last name
 separated by space) and their salaries whose salary is not
 in the range 6000 and 18000 (Begin and end values are included).
 Sort the result in ascending order by the full_name.
 Return full_name and salary.*/
 
SELECT
CONCAT(first_name," ",last_name) AS full_name,
salary
FROM employees
WHERE salary<6000 OR salary>18000
ORDER BY full_name ASC
