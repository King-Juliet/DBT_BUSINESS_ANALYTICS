
    
    

with all_values as (

    select
        age_group as value_field,
        count(*) as n_records

    from "diversifyshop"."dbt_juliet_dev"."stg_customers"
    group by age_group

)

select *
from all_values
where value_field not in (
    'Child','Youth','Young Adult','Middle Aged'
)


