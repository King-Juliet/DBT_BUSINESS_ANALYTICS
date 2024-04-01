select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select selling_price
from "diversifyshop"."dbt_juliet_dev"."stg_shop__products"
where selling_price is null



      
    ) dbt_internal_test