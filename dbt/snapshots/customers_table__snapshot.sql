{% snapshot customers_table__snapshot %}

{{
    config(
        target_database = ' '
        target_schema = 'snapshots'
        unique_key = 'customer_id',
        strategy = 'timestamp',
        updated_at = 'cust_created_at',
        invalidate_hard_delete = True
    )
}}

SELECT*FROM {{source('sourcename as configured in src file', 'customers_table')}}

{% endsnapshot %}
