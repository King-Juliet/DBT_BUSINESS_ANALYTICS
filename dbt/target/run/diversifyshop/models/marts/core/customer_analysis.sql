
  
    

  create  table "diversifyshop"."dbt_juliet_dev"."customer_analysis__dbt_tmp"
  
  
    as
  
  (
    -- This model has data that can be used for customer segmentation, 
-- customer life time value -- exploratory and predictive purpose to facilitate design of 
-- marketing strategies for each customer based on the segment they belong an possible 
--- value of the customer to the business.

SELECT
    c.customer_id,
    c.customer_location,
    c.age_group, 
    i.first_order_date, 
    i.recency, 
    i.frequency, 
    i.monetary_value, 
    i.recency_rank, 
    i.frequency_rank, 
    i.monetary_rank, 
    i.customer_segment,
    i.avg_nps,
    i.avg_csat
FROM "diversifyshop"."dbt_juliet_dev"."stg_shop__customers" AS c
LEFT JOIN "diversifyshop"."dbt_juliet_dev"."int_rfm_calc" AS i ON c.customer_id = i.customer_id
  );
  