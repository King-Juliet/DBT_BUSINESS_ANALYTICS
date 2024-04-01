select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select last_name
from "diversifyshop"."dbt_juliet_dev"."stg_shop__customers"
where last_name is null



      
    ) dbt_internal_test