select count(*) as total_rows from gold_market_daily_metrics;

select symbol, count(*) as records
from gold_market_daily_metrics
group by symbol;
