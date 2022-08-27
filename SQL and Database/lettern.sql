/*
Find all the employee's full_name(first name and
last name separated by space), employee id, and phone
number whose first name ends with the letter 'n'.*/
SELECT
employee_id,
concat(first_name," ",last_name) as full_name,

phone_number
FROM employees
where first_name like "%n";
