
  create view "diversifyshop"."dbt_juliet_dev"."stg_card_details__dbt_tmp"
    
    
  as (
    SELECT 
    cardid AS card_id,
    customerid AS customer_id,
    cardtype AS card_type,
    cardnumber AS card_number,
    created_at AS card_created_at
FROM "diversifyshop"."payments"."card_details_table"
  );