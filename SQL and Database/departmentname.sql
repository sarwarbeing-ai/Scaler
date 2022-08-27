/*Find the employee_id, employee's full name
(first and last name separated by space) as 'full_name',
salary who are working in the departments 'Administration',
'Marketing', ' Human Resources'.*/

SELECT
employee_id,
CONCAT(first_name," ",last_name) AS full_name
,salary
FROM employees
WHERE department_id IN
(SELECT
department_id
FROM departments
WHERE department_name IN ("Administration","Marketing","Human Resources"))
