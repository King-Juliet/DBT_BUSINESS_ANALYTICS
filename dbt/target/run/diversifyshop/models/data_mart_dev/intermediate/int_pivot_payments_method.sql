
  create view "diversifyshop"."dbt_juliet_dev"."int_pivot_payments_method__dbt_tmp"
    
    
  as (
    --This intermediate model is used to transform the staging payments table to into an aggregated form at the
--order_id level. Reason being that some customers may perform an order and for this single order, 
--use different payment methods to complete payment for this one order. To enable us capture this, we will
--pivot the table using CASE statement and aggregate the table using the syntax below
-- resulting table:
-- |order_id| bank_transfer_amount| card_amount| coupon_amount| gifcard_amount| total_amount
-- |        |                     |                   |              |               |WITH payment_method AS(
    SELECT*FROM {ref(stg_payments)}
),

aggregate_payment_methods_to_order_grain AS(
    SELECT
        Order_ID,
        SUM(
                CASE
                  WHEN Payment_Method = '['bank_transfer', 'card', 'coupon', 'giftcard']' AND Transaction_Status = 'completed'
                THEN Amount_Spent
                ELSE 0
            ) AS bank_transfer_amount,SUM(
                CASE
                  WHEN Payment_Method = '['bank_transfer', 'card', 'coupon', 'giftcard']' AND Transaction_Status = 'completed'
                THEN Amount_Spent
                ELSE 0
            ) AS card_amount,SUM(
                CASE
                  WHEN Payment_Method = '['bank_transfer', 'card', 'coupon', 'giftcard']' AND Transaction_Status = 'completed'
                THEN Amount_Spent
                ELSE 0
            ) AS coupon_amount,SUM(
                CASE
                  WHEN Payment_Method = '['bank_transfer', 'card', 'coupon', 'giftcard']' AND Transaction_Status = 'completed'
                THEN Amount_Spent
                ELSE 0
            ) AS giftcard_amount,
        SUM(CASE WHEN Transaction_Status = 'completed' THEN Amount_Spent) AS total_amount
        FROM payment_method
        GROUP BY 1

            )

SELECT * FROM aggregate_payment_methods_to_order_grain
  );