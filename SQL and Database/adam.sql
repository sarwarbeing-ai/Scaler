/*
Write a query to display the employee's name
 (first name and last name separated by space) as 'full_name',
 employee id,
and salary of all employees who report to Adam.*/

SELECT
employee_id,
concat(first_name," ",last_name) as full_name,
salary
FROM employees
where manager_id=(select employee_id from employees where first_name="Adam");
