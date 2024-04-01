select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    

with all_values as (

    select
        card_type as value_field,
        count(*) as n_records

    from "diversifyshop"."dbt_juliet_dev"."stg_payments__card_details"
    group by card_type

)

select *
from all_values
where value_field not in (
    'MasterCard','Visa','American Express','Discover'
)



      
    ) dbt_internal_test