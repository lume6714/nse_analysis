import pandas as pd
import yfinance as yf 
import matplotlib.pyplot as mt 

tickers=["RELIANCE.NS", "ICICIBANK.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS"]
data=yf.download(tickers, period="1y")["Close"]



print(data.head().round(2))
print(f"\nshape: {data.shape}")

returns=data.pct_change().dropna()

ann_return=returns.mean()*252
mean=returns.mean()

std=returns.std()*(252**0.5)

sharpe=ann_return/std

print(f"sharpe ratio {sharpe.round(4)}\n")
print(f"annual volatility {std.round(2)}\n")
print(f"annual returns {ann_return.round(3)}\n")
print(f"mean value {mean}\n")

cum_returns=(1+returns).cumprod()

cum_returns.plot(figsize=(12, 6), title="Cumulative Returns - NSE Stocks (1Y)")
mt.savefig("report.png")





