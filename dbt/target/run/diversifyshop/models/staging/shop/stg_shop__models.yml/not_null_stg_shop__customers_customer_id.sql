select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select customer_id
from "diversifyshop"."dbt_juliet_dev"."stg_shop__customers"
where customer_id is null



      
    ) dbt_internal_test