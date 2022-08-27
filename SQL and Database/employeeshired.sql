/*Find the details of all the employees first_name,
last_name, job_id, and hire_date who were hired between
the dates November 15th, 1998 and August 25th, 2001.*/
SELECT
first_name,
last_name,
job_id,
hire_date
FROM employees
WHERE hire_date BETWEEN "1998-11-15" AND "2001-08-25"
