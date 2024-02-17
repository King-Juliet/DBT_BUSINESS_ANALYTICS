






    with grouped_expression as (
    select
        
        
    
  
( 1=1 and csat_score >= 0 and csat_score <= 100
)
 as expression


    from "diversifyshop"."dbt_juliet_dev"."stg_customer_reviews"
    

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







