import sys
import matplotlib.pyplot as plt
import pandas as pd

# Assign arguments to descriptive variables
input_tsv = sys.argv[1]
plot_filename = sys.argv[2]
sample_size = int(sys.argv[3])

# Load dataset
results_df = pd.read_csv(input_tsv, sep="\t")

# Extract unique groups and prepare data for the boxplot
unique_k_values = sorted(results_df["k"].unique())
distribution_data = [results_df[results_df["k"] == k_val]["mean"].values for k_val in unique_k_values]
group_labels = [f"k={k_val}" for k_val in unique_k_values]

# Create the visualization
plt.figure(figsize=(12, 5))
plt.boxplot(distribution_data, tick_labels=group_labels)

# Formatting
plt.title(f"Testing Draws for {sample_size}")
plt.ylabel("Mean Value")
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Optional: adds readability
plt.tight_layout()

# Export result
plt.savefig(plot_filename, dpi=150)
