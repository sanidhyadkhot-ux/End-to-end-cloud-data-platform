select
    symbol,
    event_date,
    min(price) as low_price,
    max(price) as high_price,
    avg(price) as avg_price,
    sum(volume) as total_volume,
    sum(trade_value) as total_trade_value
from {{ ref('silver_market') }}
group by symbol, event_date
