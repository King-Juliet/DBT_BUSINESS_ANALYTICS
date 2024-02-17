
    
    

with all_values as (

    select
        payment_methods as value_field,
        count(*) as n_records

    from "diversifyshop"."dbt_juliet_dev"."stg_payments"
    group by payment_methods

)

select *
from all_values
where value_field not in (
    'bank_transfer','card','coupon','giftcard'
)


