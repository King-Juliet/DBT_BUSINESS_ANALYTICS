select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select customer_location
from "diversifyshop"."dbt_juliet_dev"."stg_customers"
where customer_location is null



      
    ) dbt_internal_test