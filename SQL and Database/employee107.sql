/*
Find the employee's details full_name (first name and last name
separated by space), salary, department id, and job id of
those employees who work the same
job as the employee with employee_id as 107.*/
SELECT
concat(first_name," ",last_name) as full_name,
salary,
department_id,
job_id
FROM employees
where job_id IN
(select job_id
from employees
where employee_id=107);
