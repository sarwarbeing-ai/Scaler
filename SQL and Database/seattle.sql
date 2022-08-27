/*
Display the employee’s first name and last name,
employee id, and job id for all employees
whose department location is in Seattle.*/
SELECT
first_name,
last_name,
employee_id,
job_id
FROM employees
where department_id IN
(SELECT
department_id
FROM departments
where location_id IN
(SELECT
location_id
FROM locations
where city="Seattle"));
