/*
Find the employee's details like first name, last name,
employee id, job id, and manager id of
those employees who are not working in any department. */
SELECT
employee_id,
first_name,
last_name,
job_id,
manager_id
FROM employees
where department_id is NULL;
