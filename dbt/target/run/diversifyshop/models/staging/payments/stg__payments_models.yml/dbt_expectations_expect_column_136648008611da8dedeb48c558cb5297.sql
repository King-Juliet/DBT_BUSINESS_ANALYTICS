select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      with relation_columns as (

        
        select
            cast('CARD_ID' as TEXT) as relation_column,
            cast('BIGINT' as TEXT) as relation_column_type
        union all
        
        select
            cast('CUSTOMER_ID' as TEXT) as relation_column,
            cast('BIGINT' as TEXT) as relation_column_type
        union all
        
        select
            cast('CARD_TYPE' as TEXT) as relation_column,
            cast('TEXT' as TEXT) as relation_column_type
        union all
        
        select
            cast('CARD_NUMBER' as TEXT) as relation_column,
            cast('BIGINT' as TEXT) as relation_column_type
        union all
        
        select
            cast('CARD_CREATED_AT' as TEXT) as relation_column,
            cast('TIMESTAMP WITHOUT TIME ZONE' as TEXT) as relation_column_type
        
        
    ),
    test_data as (

        select
            *
        from
            relation_columns
        where
            relation_column = 'CARD_TYPE'
            and
            relation_column_type not in ('VARCHAR')

    )
    select *
    from test_data
      
    ) dbt_internal_test