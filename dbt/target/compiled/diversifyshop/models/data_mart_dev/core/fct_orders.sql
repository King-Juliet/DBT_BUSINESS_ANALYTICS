-- This model contains information that can be used to perform various analysis like
-- product performance, sales analyics based on various metrics.
SELECT 
o.order_date,
o.order_id,
o.product_id,
o.customer_id,
o.order_type,
o.transaction_status,
o.unit_price,
o.quantity,
o.amount_spent,
ci.customer_location
i.customer_segment,
p.payment_methods,
c.card_type
FROM "diversifyshop"."dbt_juliet_dev"."stg_payments" AS p 
LEFT JOIN "diversifyshop"."dbt_juliet_dev"."stg_orders" AS o ON p.order_id = o.order_id
LEFT JOIN "diversifyshop"."dbt_juliet_dev"."int_rfm_calc" AS i ON o.customer_id = i.customer_id
LEFT JOIN "diversifyshop"."dbt_juliet_dev"."stg_card_details" AS c ON i.customer_id = c.customer_id
LEFT JOIN "diversifyshop"."dbt_juliet_dev"."stg_customers" AS ci ON c.customer_id = ci.customer_id