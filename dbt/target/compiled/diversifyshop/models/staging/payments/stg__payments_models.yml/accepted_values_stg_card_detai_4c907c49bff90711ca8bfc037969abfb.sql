
    
    

with all_values as (

    select
        card_type as value_field,
        count(*) as n_records

    from "diversifyshop"."dbt_juliet_dev"."stg_card_details"
    group by card_type

)

select *
from all_values
where value_field not in (
    'MasterCard','Visa','American Express','Discover'
)


