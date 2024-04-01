{% snapshot card_detail_table__snapshot %}

{{
    config(
        target_database = 'diversifyshop'
        target_schema = 'snapshots'
        unique_key = 'card_id',
        strategy = 'timestamp',
        updated_at = 'card_created_at',
        invalidate_hard_delete = True
    )
}}

SELECT*FROM {{source('payments', 'card_detail_table')}}

{% endsnapshot %}
