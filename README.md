# Crypto Market Tracker  
*(Work in Progress)*  

---

## Introduction / Goal  
This is an ongoing project where I am learning how to pull and visualize real-time cryptocurrency data using Python, SQL, and Tableau Public.  
The data comes from the free CoinGecko API, and the goal is to practice turning raw API data into something visual and easy to understand.  

Right now, the focus is on building a small dashboard that shows the top cryptocurrencies by market cap, their 24-hour price changes, and overall market trends.

---

## Dashboard Preview  
Dashboard will be added here once it is published on Tableau Public.  
A screenshot will also be added once the visuals are finalized.

---

## Table of Contents  
1. Data Overview  
2. Implementation with Python and SQL  
3. Dashboard Insights (in progress)  
4. Next Steps  
5. Resources  

---

## Data Overview  
**Source:** [CoinGecko API](https://www.coingecko.com/en/api)  
- Currency: USD  
- Fields: Coin name, symbol, current price, market cap, 24h price change, trading volume  
- Frequency: Can be updated daily  

---

## Implementation with Python and SQL  

### 1. API Extraction (Python)
```python
import requests, pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {"vs_currency":"usd","order":"market_cap_desc","per_page":10}
data = requests.get(url, params=params).json()

df = pd.DataFrame(data)[["id","symbol","current_price","market_cap","price_change_percentage_24h","total_volume"]]
df.to_csv("crypto_prices.csv", index=False)
