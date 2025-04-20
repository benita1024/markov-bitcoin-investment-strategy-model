# First, we import pandas — go-to library for handling datasets in Python
import pandas as pd

# We load the dataset from a CSV file into a DataFrame called df
df = pd.read_csv("Bitcoin Pulse  Hourly Dataset from Markets Trends and Fear.csv")

# We convert the 'timestamp' column to actual datetime objects so we can work with date-based filtering later
# If any timestamp is invalid, we coerce it to NaT (Not a Time)
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

# We now want to focus only on the data from the year 2025
# So we filter for rows where the timestamp is in 2025 and reset the index
df_2025 = df[df["timestamp"].dt.year == 2025].copy().reset_index(drop=True)

# Now we define a function that turns the Fear & Greed index into 5 distinct sentiment labels
# These labels will act as our "states" in the Markov model
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

# Apply the labeling function to the 'fear_greed_index' column to generate a new 'State' column
df_2025["State"] = df_2025["fear_greed_index"].apply(label_state)

# Define a function that calculates the transition matrix — it tracks how often we move from one state to another
def compute_matrix():
    # Start by creating a 5x5 DataFrame filled with zeros — this will count transitions from each state to every other state
    transition_counts = pd.DataFrame(0, 
                                     index=["Extreme Fear", "Fear", "Neutral", "Greed", "Extreme Greed"],
                                     columns=["Extreme Fear", "Fear", "Neutral", "Greed", "Extreme Greed"])

    # Loop through each pair of consecutive rows in the dataset
    for i in range(len(df_2025) - 1):
        # Get the current state and the next state
        from_state = df_2025.loc[i, "State"]
        to_state = df_2025.loc[i + 1, "State"]
        
        # Increment the count for this transition
        transition_counts.loc[from_state, to_state] += 1

    # Now we convert the counts into probabilities by dividing each row by its total
    transition_matrix = transition_counts.div(transition_counts.sum(axis=1), axis=0)

    # Return the final transition matrix
    return transition_matrix

# Print out the resulting transition matrix for 2025
print("Transition Matrix (2025):")
print(compute_matrix())

