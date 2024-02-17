
    
    

with all_values as (

    select
        customer_segment as value_field,
        count(*) as n_records

    from "diversifyshop"."dbt_juliet_dev"."int_rfm_calc"
    group by customer_segment

)

select *
from all_values
where value_field not in (
    'GoldMines','High Value Customers','Loyal Customer','Whales','About to lose GoldMine','About to lose HighValueCustomer','About to lose LoyalCustomer','About to lose Whales','Hibernating GoldMines','Hibernating HighValueCustomers','Hibernating LoyalCustomer','Hibernating Whales','Lost Customer','Others'
)


