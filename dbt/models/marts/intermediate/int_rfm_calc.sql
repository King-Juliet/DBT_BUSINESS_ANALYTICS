-- Intermediate model to calculate RFM Segment of each customer. To be used in models/core models
-- for analysis


WITH RFM_Data AS (
    SELECT 
        c.customer_id,
        MIN(order_date) AS first_order_date,
        MAX(o.order_date) AS last_order_date,
		TO_TIMESTAMP('2024-02-05', 'YYYY-MM-DD') - MAX(o.order_date)::TIMESTAMP AS recency,
        COUNT(DISTINCT order_id) AS frequency,
        SUM(amount_spent) AS monetary_value,
		AVG(nps_score) AS avg_nps,
		AVG(csat_score) AS avg_csat
    FROM {{ref('stg_shop__customers')}} AS c
    LEFT JOIN  {{ref('stg_shop__orders')}} AS o ON c.customer_id = o.customer_id
	LEFT JOIN {{ref('stg_shop__customer_reviews')}} AS cr ON o.customer_id = cr.customer_id
    GROUP BY c.customer_id
	
),

segments AS(
SELECT 
    customer_id,
    first_order_date,
    recency,
    frequency,
    monetary_value,
	avg_nps,
	avg_csat,
RANK() OVER(ORDER BY last_order_date DESC) AS recency_rank,
RANK() OVER(ORDER BY frequency) AS frequency_rank,
RANK()OVER(ORDER BY monetary_value) AS monetary_rank,
  CASE
	--Active WHEN  Recency <=60
		WHEN  EXTRACT(DAY FROM recency) <= 60 AND frequency >= 50 AND monetary_value >= 360000 THEN 'GoldMines'
		WHEN  EXTRACT(DAY FROM recency) <= 60 AND frequency >= 25 AND monetary_value >= 360000 THEN 'High Value Customers'
		WHEN  EXTRACT(DAY FROM recency) <= 60 AND frequency >= 25 AND monetary_value < 360000 THEN 'Loyal Customer'
		WHEN  EXTRACT(DAY FROM recency) <= 60 AND frequency < 25  AND monetary_value >= 360000 THEN 'Whales'
 -- partiallyActive WHEN  Recency > 60 AND Recency <= 120
		WHEN  EXTRACT(DAY FROM recency) > 60 AND EXTRACT(DAY FROM recency) <= 120 AND frequency >= 50 AND monetary_value >= 360000 THEN 'About to lose GoldMine'
		WHEN  EXTRACT(DAY FROM recency) > 60 AND EXTRACT(DAY FROM recency) <= 120 AND frequency >= 25 AND monetary_value >= 360000 THEN 'About to lose HighValueCustomer'
		WHEN  EXTRACT(DAY FROM recency) > 60 AND EXTRACT(DAY FROM recency) <= 120 AND frequency >= 25 AND monetary_value < 360000 THEN 'About to lose LoyalCustomer'
		WHEN  EXTRACT(DAY FROM recency) > 60 AND EXTRACT(DAY FROM recency) <= 120 AND frequency < 25  AND monetary_value >= 360000 THEN 'About to lose Whales'
	-- hybernating WHEN Recency >120 AND Recency <=365 
		WHEN EXTRACT(DAY FROM recency) > 120 AND EXTRACT(DAY FROM recency) <= 365 AND frequency >= 50 AND monetary_value >= 360000 THEN 'Hibernating GoldMines'
		WHEN EXTRACT(DAY FROM recency) > 120 AND EXTRACT(DAY FROM recency) <= 365 AND frequency >= 25 AND monetary_value >= 360000 THEN 'Hibernating HighValueCustomers'
		WHEN EXTRACT(DAY FROM recency) > 120 AND EXTRACT(DAY FROM recency) <= 365 AND frequency >= 25 AND monetary_value < 360000 THEN 'Hibernating LoyalCustomer'
		WHEN EXTRACT(DAY FROM recency) > 120 AND EXTRACT(DAY FROM recency) <= 365 AND frequency < 25  AND monetary_value >= 360000 THEN 'Hibernating Whales'
-- Lost customer WHEN Recency > 365
		WHEN EXTRACT(DAY FROM recency) > 365 THEN 'Lost Customer'
		ELSE 'Others'
	END AS customer_segment
FROM RFM_Data
)

SELECT*FROM segments


