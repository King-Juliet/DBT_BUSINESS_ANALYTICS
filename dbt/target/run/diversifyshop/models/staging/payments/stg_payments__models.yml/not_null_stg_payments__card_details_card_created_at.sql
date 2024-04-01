select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select card_created_at
from "diversifyshop"."dbt_juliet_dev"."stg_payments__card_details"
where card_created_at is null



      
    ) dbt_internal_test