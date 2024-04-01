{% snapshot products_table__snapshot %}

{{
    config(
        target_database = 'diversifyshop'
        target_schema = 'snapshots'
        unique_key = 'product_id',
        strategy = 'timestamp',
        updated_at = 'prod_created_at',
        invalidate_hard_delete = True
    )
}}

SELECT*FROM {{source('payments', 'products_table')}}

{% endsnapshot %}
