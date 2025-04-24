## Bitcoin Sentiment Strategy CLI: A Markov Chain Simulator of Bitcoin Market Sentiment

This project models Bitcoin price behavior across Fear & Greed sentiment regimes using a Markov chain framework. By labeling each hourly data point with a sentiment state, computing average prices per state, and building a transition matrix, you can interactively test “buy in X, sell in Y” strategies and immediately see historical return ratios.

## Objective

To explore how sentiment‐based trading decisions drive returns by simulating state transitions in a Markov chain over historical Bitcoin price data.

## How It Works

1. **Load data**  
   Read the hourly CSV of Bitcoin prices paired with the Fear & Greed Index.  
2. **Label states**  
   Map each hour to one of five sentiment states: Extreme Fear, Fear, Neutral, Greed, Extreme Greed.  
3. **Compute averages**  
   Calculate the average Bitcoin price observed in each sentiment state.  
4. **Build transition matrix**  
   Construct a 5×5 Markov matrix that records the probability of moving from one sentiment state to another on the next hour.  
5. **Interactive CLI**  
   Prompt the user to select a “buy” sentiment and a “sell” sentiment from the menu.  
6. **Calculate return**  
   Fetch the two state averages, compute the return ratio \((P_{\text{sell}} - P_{\text{buy}})/P_{\text{buy}}\), and display an emoji‐driven assessment of strategy strength.

## Features

- **Custom sentiment states**  
  Five preconfigured regimes matching the Fear & Greed Index—easy to adjust or extend.  
- **Precomputed statistics**  
  Average prices and transition probabilities are calculated once on startup for maximum responsiveness.  
- **Markov chain insights**  
  See not only average‐price gaps but also state transition dynamics for deeper analysis.  
- **Interactive CLI**  
  Menu‐driven, zero‐code interface—ideal for rapid strategy prototyping or classroom demos.  
- **Emoji feedback**  
  Instantly know if your chosen strategy is historically strong, reasonable, marginal, or a loss.

## Getting Started

Clone the repo and enter its directory:
```bash
git clone https://github.com/yourusername/bitcoin-markov.git
cd bitcoin-markov
pip install -r requirements.txt
python cli.py
