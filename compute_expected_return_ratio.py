"""
This code calculates the expected return ratios for sentiment-based Bitcoin investment strategies
using a Markov Chain model. It imports:

- A transition matrix from BitcoinStrategy.py, representing state-to-state sentiment probabilities
- Average Bitcoin prices per sentiment state from compute_avg_price_per_state.py

For each unique shortest sentiment transition path (e.g., Fear → Greed), the script:
- Computes the path's overall transition probability by multiplying individual step probabilities
- Calculates the return ratio based on average prices
- Computes the expected return = probability × return ratio

The output is a sorted table showing the most promising sentiment-based trading strategies.
"""

import pandas as pd
import networkx as nx
from compute_avg_price_per_state import compute_avg_price_per_state
from BitcoinStrategy import compute_matrix

def compute_expected_returns(csv_path):
    # Load data from dependencies
    avg_prices = compute_avg_price_per_state(csv_path)
    transition_matrix = compute_matrix()

    states = ["Extreme Fear", "Fear", "Neutral", "Greed", "Extreme Greed"]

    # Build sentiment transition graph
    G = nx.DiGraph()
    for i in range(len(states) - 1):
        G.add_edge(states[i], states[i + 1])
        G.add_edge(states[i + 1], states[i])

    results = []
    for from_state in states:
        for to_state in states:
            if from_state != to_state:
                try:
                    path = nx.shortest_path(G, from_state, to_state)
                    prob = 1.0
                    for i in range(len(path) - 1):
                        prob *= transition_matrix.loc[path[i], path[i + 1]]
                    return_ratio = (avg_prices[to_state] - avg_prices[from_state]) / avg_prices[from_state]
                    expected_return = prob * return_ratio
                    results.append({
                        "From": from_state,
                        "To": to_state,
                        "Transition Probability": round(prob, 6),
                        "Return Ratio": round(return_ratio, 6),
                        "Expected Return": round(expected_return, 6)
                    })
                except:
                    continue

    df = pd.DataFrame(results)
    df["From"] = pd.Categorical(df["From"], categories=states, ordered=True)
    return df.sort_values(by=["From", "To"])

if __name__ == "__main__":
    csv_path = "Bitcoin Pulse  Hourly Dataset from Markets Trends and Fear.csv"
    df = compute_expected_returns(csv_path)
    pd.set_option('display.float_format', lambda x: '%.6f' % x)
    print(df.to_string(index=False))
