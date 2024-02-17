SELECT 
    paymentid AS payment_id,
    orderid AS order_id,
    paymentmethod AS payment_methods,
    paymentdate AS payment_date
FROM {{source('payments', 'payments_table')}}

