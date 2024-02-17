




    with grouped_expression as (
    select
        
        
    
  


    

coalesce(array_length((select regexp_matches(email, '^[A-Z0-9+_.-]+@[A-Z0-9.-]+$', '')), 1), 0)


 > 0
 as expression


    from "diversifyshop"."dbt_juliet_dev"."stg_customers"
    

),
validation_errors as (

    select
        *
    from
        grouped_expression
    where
        not(expression = true)

)

select *
from validation_errors




