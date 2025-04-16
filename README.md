# Modeling Bitcoin Market Behavior with a Sentiment-Driven Markov Chain

## Overview
This project analyzes Bitcoin market behavior using a 5-state Markov model based on the Fear & Greed Index. It compares two sentiment-driven investment strategies by calculating transition probabilities and expected returns using real BTC price data.

## Sentiment States
- Extreme Fear (0–25)
- Fear (26–45)
- Neutral (46–60)
- Greed (61–75)
- Extreme Greed (76–100)

## Timeframe
- January 1, 2025 – April 7, 2025

## Strategy Definitions
**Strategy A**: Buy in Extreme Fear, Sell in Neutral  
**Strategy B**: Buy in Fear, Sell in Greed

Returns are calculated using:
- (sell_price - buy_price) / buy_price

## Key Actions
1. Build transition matrix using hourly sentiment changes
2. Compute average BTC price per sentiment state
3. Calculate return ratios for transitions
4. Simulate strategies to assess expected returns
5. Compare performance using 2025 data and validate with 2024 data

## Tools
- Python (Pandas, NetworkX)
- CSV dataset of hourly sentiment and BTC price

## Planned Features
- Command-line tool to compare custom strategies
- Output: expected return, probability, and performance summary
