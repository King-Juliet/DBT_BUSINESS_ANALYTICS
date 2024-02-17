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
ci.customer_location,
i.customer_segment,
p.payment_methods,
c.card_type
FROM {{ref('stg_shop__orders')}} AS o
LEFT JOIN {{ref('stg_payments')}} AS p ON o.order_id = p.order_id
--FROM {{ref('stg_payments')}} AS p 
--LEFT JOIN {{ref('stg_shop__orders')}} AS o ON p.order_id = o.order_id
LEFT JOIN {{ref('int_rfm_calc')}} AS i ON o.customer_id = i.customer_id
LEFT JOIN {{ref('stg_payments__card_details')}} AS c ON i.customer_id = c.customer_id
LEFT JOIN {{ref('stg_shop__customers')}} AS ci ON c.customer_id = ci.customer_id

 
