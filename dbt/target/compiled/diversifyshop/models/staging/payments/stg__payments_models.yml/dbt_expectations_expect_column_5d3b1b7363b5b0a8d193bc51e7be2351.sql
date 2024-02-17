




    with grouped_expression as (
    select
        
        
    
  

    length(
        card_number
    ) = 16 as expression


    from "diversifyshop"."dbt_juliet_dev"."stg_card_details"
    

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




