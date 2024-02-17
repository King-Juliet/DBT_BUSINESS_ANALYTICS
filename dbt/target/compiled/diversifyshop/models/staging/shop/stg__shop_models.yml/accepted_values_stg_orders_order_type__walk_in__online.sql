
    
    

with all_values as (

    select
        order_type as value_field,
        count(*) as n_records

    from "diversifyshop"."dbt_juliet_dev"."stg_orders"
    group by order_type

)

select *
from all_values
where value_field not in (
    'walk-in','online'
)


