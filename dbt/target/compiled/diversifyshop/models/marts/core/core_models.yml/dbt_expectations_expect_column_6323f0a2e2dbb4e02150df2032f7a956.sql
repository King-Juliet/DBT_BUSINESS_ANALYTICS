






    with grouped_expression as (
    select
        
        
    
  
( 1=1 and nps_score >= 0 and nps_score <= 10
)
 as expression


    from "diversifyshop"."dbt_juliet_dev"."customer_reviews"
    

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







