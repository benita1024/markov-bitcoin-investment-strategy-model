import pandas as pd
import matplotlib.pyplot as plt
from compute_avg_price_per_state import compute_avg_price_per_state

# 1. Load the 2025 average prices per sentiment state
csv_path = "Bitcoin Pulse  Hourly Dataset from Markets Trends and Fear.csv"
avg_prices = compute_avg_price_per_state(csv_path)

# 2. Build the return‑ratio DataFrame
states = avg_prices.index.tolist()
rows = []
for A in states:
    for B in states:
        if A != B:
            rr = (avg_prices[B] - avg_prices[A]) / avg_prices[A] * 100
            rows.append([A, B, round(rr, 2)])
df_rr = pd.DataFrame(rows, columns=["From", "To", "Return Ratio (%)"])

# 3. Render the table as an image
fig, ax = plt.subplots(figsize=(8, len(df_rr)*0.25 + 1))  # height scales with rows
ax.axis("off")  # no axes for a clean table

# Create the table
tbl = ax.table(
    cellText=df_rr.values,
    colLabels=df_rr.columns,
    cellLoc="center",
    loc="center"
)

# Styling
tbl.auto_set_font_size(False)
tbl.set_fontsize(10)
tbl.scale(1, 1.5)

plt.tight_layout()

# 4. Save to separate files
plt.savefig("return_ratios_table.png", dpi=300, bbox_inches="tight")  # for web/poster
plt.savefig("return_ratios_table.pdf", bbox_inches="tight")           # for print
plt.close(fig)
