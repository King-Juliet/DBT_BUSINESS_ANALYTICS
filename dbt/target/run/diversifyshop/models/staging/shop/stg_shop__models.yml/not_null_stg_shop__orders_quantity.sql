select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select quantity
from "diversifyshop"."dbt_juliet_dev"."stg_shop__orders"
where quantity is null



      
    ) dbt_internal_test