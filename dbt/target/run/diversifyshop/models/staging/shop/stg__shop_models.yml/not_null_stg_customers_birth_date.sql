select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select birth_date
from "diversifyshop"."dbt_juliet_dev"."stg_customers"
where birth_date is null



      
    ) dbt_internal_test