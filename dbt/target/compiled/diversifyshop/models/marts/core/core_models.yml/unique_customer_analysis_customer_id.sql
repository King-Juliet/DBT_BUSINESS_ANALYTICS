
    
    

select
    customer_id as unique_field,
    count(*) as n_records

from "diversifyshop"."dbt_juliet_dev"."customer_analysis"
where customer_id is not null
group by customer_id
having count(*) > 1


