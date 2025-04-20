import pandas as pd
from compute_avg_price_per_state import compute_avg_price_per_state
from BitcoinStrategy import compute_matrix

# Load data once
CSV_PATH = "Bitcoin Pulse  Hourly Dataset from Markets Trends and Fear.csv"
avg_prices = compute_avg_price_per_state(CSV_PATH)
transition_matrix = compute_matrix()

# Ordered list of valid states
states = ["Extreme Fear", "Fear", "Neutral", "Greed", "Extreme Greed"]

# Display menu
def print_menu():
    print("\nAvailable Sentiment States:")
    for i, state in enumerate(states):
        print(f"{i + 1}. {state}")

def get_state_input(prompt):
    while True:
        try:
            choice = int(input(prompt))
            if 1 <= choice <= len(states):
                return states[choice - 1]
            else:
                print("Invalid choice. Please select a number from the list.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("Welcome to the Bitcoin Sentiment Strategy CLI Demo")
    print_menu()

    buy_state = get_state_input("\nSelect your BUY sentiment state (1-5): ")
    sell_state = get_state_input("Select your SELL sentiment state (1-5): ")

    # Check if strategy is valid
    if buy_state == sell_state:
        print("\nBuy and sell state are the same. No return expected.")
        return

    # Calculate return ratio
    try:
        buy_price = avg_prices[buy_state]
        sell_price = avg_prices[sell_state]
        return_ratio = (sell_price - buy_price) / buy_price

        print(f"\nReturn Ratio for buying in '{buy_state}' and selling in '{sell_state}': {return_ratio:.6f}")

        if return_ratio > 0.10:
            print("\U0001F4B0 This looks like a strong strategy based on historical sentiment averages!")
        elif return_ratio > 0.03:
            print("\U0001F914 Reasonable gain, but not extraordinary.")
        elif return_ratio > 0:
            print("\U0001F610 Small return — might not be worth the risk.")
        else:
            print("\u26A0\uFE0F This strategy historically leads to a loss.")

    except KeyError:
        print("Invalid state input. Please check the sentiment state names.")

if __name__ == "__main__":
    main()
