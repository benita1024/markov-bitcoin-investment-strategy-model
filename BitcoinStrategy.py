import pandas as pd

# Load your dataset
df = pd.read_csv("Bitcoin Pulse  Hourly Dataset from Markets Trends and Fear.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

# Filter only 2025 data and reset index
df_2025 = df[df["timestamp"].dt.year == 2025].copy().reset_index(drop=True)

# Define 5 sentiment states
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

# Label states
df_2025["State"] = df_2025["fear_greed_index"].apply(label_state)

def compute_matrix():
    # Calculate proper transition matrix using actual transitions
    transition_counts = pd.DataFrame(0, index=["Extreme Fear", "Fear", "Neutral", "Greed", "Extreme Greed"],
                                    columns=["Extreme Fear", "Fear", "Neutral", "Greed", "Extreme Greed"])

    for i in range(len(df_2025) - 1):
        from_state = df_2025.loc[i, "State"]
        to_state = df_2025.loc[i + 1, "State"]
        transition_counts.loc[from_state, to_state] += 1

    # Normalize to probabilities
    transition_matrix = transition_counts.div(transition_counts.sum(axis=1), axis=0)

    return transition_matrix
#print("Corrected Transition Matrix (2025):")
#print(compute_matrix())
