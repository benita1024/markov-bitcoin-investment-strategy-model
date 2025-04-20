import pandas as pd

def compute_avg_price_per_state(csv_path):
    # 1) Load and parse timestamps
    df = pd.read_csv(csv_path)
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    # Debug: show what years are present
    print("Data covers years:", sorted(df["timestamp"].dt.year.dropna().unique()))

    # 2) Filter for 2025 only
    df_2025 = df[df["timestamp"].dt.year == 2025].copy()
    print(f"Entries in 2025: {len(df_2025)} (from {df_2025['timestamp'].min()} to {df_2025['timestamp'].max()})")

    # 3) Define sentiment bins
    def label_state(idx):
        if idx <= 25:
            return "Extreme Fear"
        elif idx <= 45:
            return "Fear"
        elif idx <= 60:
            return "Neutral"
        elif idx <= 75:
            return "Greed"
        else:
            return "Extreme Greed"

    # 4) Apply labels
    df_2025["State"] = df_2025["fear_greed_index"].apply(label_state)

    # 5) Compute and print average prices per state
    states = ["Extreme Fear","Fear","Neutral","Greed","Extreme Greed"]
    avg_prices = (
        df_2025
        .groupby("State")["BTC_USDT_1h_close"]
        .mean()
        .reindex(states)
    )
    print("\n2025 average prices by state:")
    print(avg_prices.to_string())

    return avg_prices

def print_return_ratios(csv_path):
    avg_prices = compute_avg_price_per_state(csv_path)

    # Build the 20 return ratios
    states = avg_prices.index.tolist()
    rows = []
    for A in states:
        for B in states:
            if A == B:
                continue
            rr = (avg_prices[B] - avg_prices[A]) / avg_prices[A]
            rows.append({
                "From": A,
                "To": B,
                "Return Ratio (%)": round(rr * 100, 2)
            })

    df_rr = pd.DataFrame(rows).sort_values(["From","To"]).reset_index(drop=True)
    print("\nAll Return Ratios (2025):")
    print(df_rr.to_string(index=False))

if __name__ == "__main__":
    csv_path = "Bitcoin Pulse  Hourly Dataset from Markets Trends and Fear.csv"
    print_return_ratios(csv_path)
