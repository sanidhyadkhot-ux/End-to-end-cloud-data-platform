select * from {{ source('raw', 'asx_market_ticks') }}
