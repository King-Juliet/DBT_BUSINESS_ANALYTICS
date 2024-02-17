select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select review_date
from "diversifyshop"."dbt_juliet_dev"."stg_customer_reviews"
where review_date is null



      
    ) dbt_internal_test