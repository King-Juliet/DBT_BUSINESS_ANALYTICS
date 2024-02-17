--This intermediate model is used to transform the staging payments table to into an aggregated form at the
--order_id level. Reason being that some customers may perform an order and for this single order, 
--use different payment methods to complete payment for this one order. To enable us capture this, we will
--pivot the table using CASE statement and aggregate the table using the syntax below
-- resulting table:
-- |order_id| bank_transfer_amount| card_amount| coupon_amount| gifcard_amount| total_amount
-- |        |                     |                   |              |               | 

--{% set Payment_Methods = ["bank_transfer", "card", "coupon", "giftcard"] %}

--WITH payment_method AS(
    --SELECT*FROM {{ref('stg_payments')}}
--)

--aggregate_payment_methods_to_order_grain AS(
    --SELECT
        --Order_ID,
        --{% for Payment_Method in Payment_Methods -%}
            --SUM(
                --CASE
                  --WHEN Payment_Method = '{{Payment_Methods}}' AND Transaction_Status = 'completed'
                --THEN Amount_Spent
                --ELSE 0
            --) AS {{Payment_Method}}_amount, 
           
        --{%- endfor %}
        --SUM(CASE WHEN Transaction_Status = 'completed' THEN Amount_Spent) AS total_amount
        --FROM {{ref('stg_payments')}}
        --FROM payment_method
        --GROUP BY 1

            --)

--SELECT * FROM aggregate_payment_methods_to_order_grain

{% set Payment_Methods = ["bank_transfer", "card", "coupon", "giftcard"] %}

SELECT
    {{ref('stg_shop__orders')}}.order_id,
    amount_spent,
    transaction_status,
    {% for Payment_Method in Payment_Methods -%}
        SUM(
            CASE
              WHEN payment_methods = '{{Payment_Method}}' AND transaction_status = 'completed'
              THEN amount_spent
              ELSE 0
            END
        ) AS {{Payment_Method}}_amount,
    {% endfor %}
    SUM(amount_spent) AS total_amount
    --SUM(CASE WHEN transaction_status = 'completed' THEN amount_spent ELSE 0 END) AS total_amount
FROM {{ref('stg_payments')}}
LEFT JOIN {{ref('stg_shop__orders')}} ON {{ref('stg_payments')}}.order_id = {{ref('stg_shop__orders')}}.order_id
GROUP BY {{ref('stg_shop__orders')}}.order_id, amount_spent, transaction_status

