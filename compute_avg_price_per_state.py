import pandas as pd

def compute_avg_price_per_state(csv_path):
    """
    Computes the average Bitcoin price in 2025 for each sentiment state
    based on the BTC_USDT_1h_close column and the fear_greed_index.
    
    Parameters:
        csv_path (str): Path to the CSV file
    
    Returns:
        pandas.Series: Average BTC price per sentiment state
    """
    # Load dataset
    df = pd.read_csv(csv_path)
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    # Filter for 2025 only
    df_2025 = df[df["timestamp"].dt.year == 2025].copy()

    # Define labeling function
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

    # Apply state labels
    df_2025["State"] = df_2025["fear_greed_index"].apply(label_state)

    # Calculate average BTC price per state
    avg_prices = df_2025.groupby("State")["BTC_USDT_1h_close"].mean().sort_index()

    return avg_prices


# Run main only if this file is executed directly
if __name__ == "__main__":
    #File path to your CSV
    csv_path = "Bitcoin Pulse  Hourly Dataset from Markets Trends and Fear.csv"

    # Call the function
    avg_prices = compute_avg_price_per_state(csv_path)

    # Print the result
    print("Average BTC Price per Sentiment State (2025):")
    print(avg_prices)

