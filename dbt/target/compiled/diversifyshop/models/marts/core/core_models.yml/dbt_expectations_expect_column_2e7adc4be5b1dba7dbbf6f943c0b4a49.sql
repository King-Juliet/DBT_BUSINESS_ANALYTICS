






    with grouped_expression as (
    select
        
        
    
  
( 1=1 and avg_csat_score >= 0 and avg_csat_score <= 100
)
 as expression


    from "diversifyshop"."dbt_juliet_dev"."customer_analysis"
    

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







