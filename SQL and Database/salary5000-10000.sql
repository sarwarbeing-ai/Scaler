/*
Display the details of employees like employee_id,
first_name, last_name, salary who work in the departments
50,10 or 80 and salary is between 5000 to 10000 and
also where employees have no commission_pct .*/
SELECT
employee_id,
first_name,last_name,
salary
FROM employees
where (department_id IN (10,50,80)) AND (salary BETWEEN 5000 AND 10000)
AND (commission_pct IS NULL)
