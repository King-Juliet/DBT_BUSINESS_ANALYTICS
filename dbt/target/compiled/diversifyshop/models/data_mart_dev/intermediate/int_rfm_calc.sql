-- Intermediate model to calculate RFM Segment of each customer. To be used in models/core models
-- for analysis


WITH RFM_Data AS (
    SELECT 
        c.customer_id,
        MIN(order_date) AS first_order_date,
        MAX(o.order_date) AS last_order_date,
        COUNT(DISTINCT order_id) AS order_frequency,
        SUM(amount_spent) AS monetary_value,
		AVG(nps_score) AS avg_nps,
		AVG(csat_score) AS avg_csat
    FROM "diversifyshop"."dbt_juliet_dev"."stg_customers" AS c
    LEFT JOIN  "diversifyshop"."dbt_juliet_dev"."stg_orders" AS o ON c.customer_id = o.customer_id
	LEFT JOIN "diversifyshop"."dbt_juliet_dev"."stg_customer_reviews" AS cr ON o.customer_id = cr.customer_id
    GROUP BY c.customer_id
	
)

SELECT 
    customer_id,
    first_order_date,
    TO_TIMESTAMP('2024-02-05', 'YYYY-MM-DD') - last_order_date AS recency,
    frequency,
    monetary_value,
	avg_nps,
	avg_nps,
RANK() OVER(ORDER BY last_order_date DESC) recency_rank,
RANK() OVER(ORDER BY Order_Frequency) AS frequency_rank,
RANK( OVER(ORDER BY Monetary_Value)) AS monetary_rank,
  CASE
	--Active WHEN  Recency <=60
		WHEN  recency <=60 AND frequency >= 50 AND monetary_value >= 360000 THEN 'GoldMines'
		WHEN  recency <=60 AND frequency >= 25 AND monetary_value >= 360000 THEN 'High Value Customers'
		WHEN  recency <=60 AND frequency >= 25 AND monetary_value <360000 THEN 'Loyal Customer'
		WHEN  recency <=60 AND frequency <25  AND monetary_value >= 360000 THEN 'Whales'
 -- partiallyActive WHEN  Recency > 60 AND Recency <= 120
		WHEN  recency > 60 AND recency <= 120 AND frequency >= 50 AND monetary_value >= 360000 THEN 'About to lose GoldMine'
		WHEN  recency > 60 AND recency <= 120 AND frequency >= 25 AND monetary_value >= 360000 THEN 'About to lose HighValueCustomer'
		WHEN  recency > 60 AND recency <= 120 AND frequency >= 25 AND monetary_value <360000 THEN 'About to lose LoyalCustomer'
		WHEN  recency > 60 AND recency <= 120 AND frequency <25  AND monetary_value >= 360000 THEN 'About to lose Whales'
	-- hybernating WHEN Recency >120 AND Recency <=365 
		WHEN recency >120 AND recency <=365 AND frequency >= 50 AND monetary_value >= 360000 THEN 'Hibernating GoldMines'
		WHEN recency >120 AND recency <=365 AND frequency >= 25 AND monetary_value >= 360000 THEN 'Hibernating HighValueCustomers'
		WHEN recency >120 AND recency <=365 AND frequency >= 25 AND monetary_value <360000 THEN 'Hibernating LoyalCustomer'
		WHEN recency >120 AND recency <=365 AND frequency <25  AND monetary_value >= 360000 THEN 'Hibernating Whales'
-- Lost customer WHEN Recency > 365
		WHEN recency > 365 THEN 'Lost Customer'
		ELSE 'Others'
	END AS 'customer_segment'
FROM RFM_Data;