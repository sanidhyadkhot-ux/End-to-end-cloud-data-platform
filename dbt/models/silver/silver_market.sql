select
    cast(event_timestamp as timestamp) as event_timestamp,
    symbol,
    cast(price as numeric) as price,
    cast(volume as numeric) as volume,
    cast(trade_value as numeric) as trade_value,
    cast(event_date as date) as event_date
from {{ ref('bronze_market') }}
where price > 0 and volume > 0
