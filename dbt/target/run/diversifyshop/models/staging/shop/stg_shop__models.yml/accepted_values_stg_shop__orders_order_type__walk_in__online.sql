select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    

with all_values as (

    select
        order_type as value_field,
        count(*) as n_records

    from "diversifyshop"."dbt_juliet_dev"."stg_shop__orders"
    group by order_type

)

select *
from all_values
where value_field not in (
    'walk-in','online'
)



      
    ) dbt_internal_test