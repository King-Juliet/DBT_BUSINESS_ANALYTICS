select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select payment_id
from "diversifyshop"."dbt_juliet_dev"."stg_payments"
where payment_id is null



      
    ) dbt_internal_test