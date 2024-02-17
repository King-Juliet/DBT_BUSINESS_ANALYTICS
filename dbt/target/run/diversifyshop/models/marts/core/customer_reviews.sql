
  
    

  create  table "diversifyshop"."dbt_juliet_dev"."customer_reviews__dbt_tmp"
  
  
    as
  
  (
    SELECT*FROM "diversifyshop"."dbt_juliet_dev"."stg_shop__customer_reviews"
  );
  