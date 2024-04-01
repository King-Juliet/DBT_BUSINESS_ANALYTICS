
    
    

with all_values as (

    select
        transaction_status as value_field,
        count(*) as n_records

    from "diversifyshop"."dbt_juliet_dev"."stg_shop__orders"
    group by transaction_status

)

select *
from all_values
where value_field not in (
    'completed','cancelled'
)


