SELECT 
    reviewid AS review_id,
    customerid AS customer_id,
    rating_nps AS nps_score,
    rating_csat AS csat_score,
    comment AS  reviews,
    reviewdate AS review_date
FROM {{source('shop', 'customer_reviews_table')}}

    