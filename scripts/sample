import sys
import numpy as np

# Parse command line arguments into descriptive variables
max_range = int(sys.argv[1])
sample_count = int(sys.argv[2])
iterations = int(sys.argv[3])
base_seed = int(sys.argv[4])
results_path = sys.argv[5]

# Initialize generator using the provided seed and k-offset
gen = np.random.default_rng(base_seed + sample_count)

# Execute simulation and write results to file
with open(results_path, "w") as target_file:
    # Write header
    target_file.write("k\trepeat\tmean\n")
    
    for i in range(iterations):
        # Generate random integers between 1 and max_range (inclusive)
        draws = gen.integers(1, max_range + 1, size=sample_count)
        
        # Calculate the average and log the results
        average = draws.mean()
        target_file.write(f"{sample_count}\t{i}\t{average}\n")
