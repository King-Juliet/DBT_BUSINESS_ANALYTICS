
  create view "diversifyshop"."dbt_juliet_dev"."stg_payments__dbt_tmp"
    
    
  as (
    SELECT 
    paymentid AS payment_id,
    orderid AS order_id,
    paymentmethod AS payment_methods,
    paymentdate AS payment_date
FROM "diversifyshop"."payments"."payments_table"
  );