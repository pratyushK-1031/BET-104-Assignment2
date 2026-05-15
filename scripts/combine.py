import sys
import pandas as pd

# Extract the destination path and the list of source files from command line arguments
destination_file = sys.argv[1]
source_files = sys.argv[2:]

# Load each TSV file into a list of DataFrames
dataframe_list = [pd.read_csv(filepath, sep="\t") for filepath in source_files]

# Merge all DataFrames and export the result to the specified destination
pd.concat(dataframe_list).to_csv(destination_file, sep="\t", index=False)
