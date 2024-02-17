SELECT 
    CAST(orderid AS INTEGER) AS order_id,
    orderdate AS order_date,
    customerid AS customer_id,
    unitprice AS unit_price,
    quantity AS quantity,
    productid AS product_id,
    ordertype AS order_type,
    status AS transaction_status,
    quantity*unitPrice AS amount_spent
FROM "diversifyshop"."shop"."orders_table"