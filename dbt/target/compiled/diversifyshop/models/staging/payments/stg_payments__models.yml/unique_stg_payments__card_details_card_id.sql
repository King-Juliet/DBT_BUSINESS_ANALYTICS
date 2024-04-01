
    
    

select
    card_id as unique_field,
    count(*) as n_records

from "diversifyshop"."dbt_juliet_dev"."stg_payments__card_details"
where card_id is not null
group by card_id
having count(*) > 1


