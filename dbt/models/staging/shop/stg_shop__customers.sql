SELECT 
    customerid AS customer_id,
    firstname AS first_name,
    lastname AS last_name,
    INITCAP(CONCAT(firstname, ' ', lastname)) AS customer_name,
    INITCAP(gender) AS gender,
    email AS email,
    phonenumber AS phone_number,
    INITCAP(location) AS customer_location,
    birthdate AS birth_date,
    EXTRACT(YEAR FROM AGE(current_date, birthdate)) AS customer_age,
    CASE 
     WHEN EXTRACT(YEAR FROM AGE(current_date, birthdate)) BETWEEN 0 AND 14 THEN 'Child'
     WHEN EXTRACT(YEAR FROM AGE(current_date, birthdate)) BETWEEN 15 AND 24 THEN 'Youth'
     WHEN EXTRACT(YEAR FROM AGE(current_date, birthdate)) BETWEEN 25 AND 49 THEN 'Young Adult'
     WHEN EXTRACT(YEAR FROM AGE(current_date, birthdate)) BETWEEN 50 AND 65 THEN 'Middle Aged'
     ELSE 'Elderly'
    END AS age_group,
    created_at AS cust_created_at
FROM {{source('shop', 'customers_table')}}
