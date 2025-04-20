import pandas as pd
import matplotlib.pyplot as plt

def compute_avg_price_per_state(csv_path):
    """
    Reads Bitcoin dataset and calculates average price per sentiment state.
    Returns a Series with average BTC prices for each state in 2025.
    """
    # Load the dataset
    df = pd.read_csv(csv_path)
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    # Filter data for 2025
    df_2025 = df[df["timestamp"].dt.year == 2025].copy()

    # Define sentiment state based on fear/greed index
    def label_state(index):
        if index <= 25:
            return "Extreme Fear"
        elif index <= 45:
            return "Fear"
        elif index <= 60:
            return "Neutral"
        elif index <= 75:
            return "Greed"
        else:
            return "Extreme Greed"

    # Label the states
    df_2025["State"] = df_2025["fear_greed_index"].apply(label_state)

    # Group by state and calculate the average BTC price
    avg_prices = df_2025.groupby("State")["BTC_USDT_1h_close"].mean().sort_index()

    return avg_prices

# Replace with your actual CSV path
csv_path = "Bitcoin Pulse  Hourly Dataset from Markets Trends and Fear.csv"

# Compute the average prices per sentiment state
avg_prices = compute_avg_price_per_state(csv_path)

# Create a bar chart and save it
plt.figure(figsize=(10, 6))
avg_prices.plot(kind='bar', color='royalblue', edgecolor='black')
plt.title("Average BTC Price per Sentiment State (2025)", fontsize=14)
plt.xlabel("Sentiment State")
plt.ylabel("Average BTC Price (USDT)")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save the plot to files (you can choose PNG, PDF, or both)
plt.savefig("avg_price_per_sentiment_2025.png", dpi=300)  # high-res image
plt.savefig("avg_price_per_sentiment_2025.pdf")           # vector-based for posters

plt.show()
