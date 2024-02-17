{% docs customer_segment %}

One of the following values:

-------------------------------------------------------------------------------------------------  
| Customer_Segment                    | Recency (days) | Frequency        | MonetaryValue ($)    |
------------------------------------------------------------------------------------------------- 
| GoldMines                           | <=60            | >= 50            | >= 360000           |
| High Value Customers                | <=60            | >= 25            | >= 360000           |
| Loyal Customer                      | <=60            | >= 25            | <360000             |
| Whales                              | <=60            | <25              | >= 360000           |
| About to lose GoldMine              | > 60 AND <= 120 | >= 50            | >= 360000           |
| About to lose HighValueCustomer     | > 60 AND <= 120 | >= 25            | >= 360000           |
| About to lose LoyalCustomer         | >60 AND <= 120  | >= 25            | <360000             |
| About to lose Whales                | >60 AND <= 120  | <25              | >= 360000           |
| Hibernating GoldMines               | >120 AND <=365  | >= 50            | >= 360000           |
| Hibernating HighValueCustomers      | >120 AND <=365  | >= 25            |>= 360000            |
| Hibernating LoyalCustomer           | >120 AND <=365  | >= 25            | <360000             |
| Hibernating Whales                  | >120 AND <=365  | <25              | >= 360000           |
| Lost Customer                       | > 365           | Any number       | Any number          |
| Others                              | Does not fit into any of the categories .    
---------------------------------------------------------------------------------------------------

{% enddocs %}