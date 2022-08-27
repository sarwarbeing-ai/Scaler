/*
Display all the details of the employees who did
not work at any job in the past. */
SELECT
*
FROM employees
where employee_id NOT IN
(SELECT
employee_id
FROM job_history )
