/*
Using the employee's table, make a new column as 'Accountant'
if the employees are working as the 'FI_ACCOUNT' or 'AC_ACCOUNT'
designation. label it as 1 else as 0. */
SELECT
employee_id,
first_name,last_name,
salary,
CASE
    WHEN job_id IN ("FI_ACCOUNT" ,"AC_ACCOUNT")
    THEN 1
    ELSE 0
END AS Accountant
FROM employees
