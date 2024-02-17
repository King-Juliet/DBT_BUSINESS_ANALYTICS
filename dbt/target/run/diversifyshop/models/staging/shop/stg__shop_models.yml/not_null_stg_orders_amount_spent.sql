select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select amount_spent
from "diversifyshop"."dbt_juliet_dev"."stg_orders"
where amount_spent is null



      
    ) dbt_internal_test