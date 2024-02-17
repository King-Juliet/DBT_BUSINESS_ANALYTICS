
    
    

select
    review_id as unique_field,
    count(*) as n_records

from "diversifyshop"."dbt_juliet_dev"."stg_customer_reviews"
where review_id is not null
group by review_id
having count(*) > 1


