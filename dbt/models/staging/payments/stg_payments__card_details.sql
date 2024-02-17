SELECT 
    cardid AS card_id,
    customerid AS customer_id,
    cardtype AS card_type,
    cardnumber AS card_number,
    created_at AS card_created_at
FROM {{source('payments', 'card_details_table')}}
