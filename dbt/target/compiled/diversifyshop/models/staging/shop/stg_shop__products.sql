SELECT 
    productid AS product_id,
    name AS product_name,
    description AS product_description,
    unitprice AS selling_price,
    created_at AS prod_created_at
FROM "diversifyshop"."shop"."products_table"