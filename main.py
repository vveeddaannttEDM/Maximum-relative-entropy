from mre_model import MaximumRelativeEntropy
import pandas as pd

# Load sample data
data = pd.read_csv('data/sample_data.csv')

# Define moment constraints (expected average type of balls)
expected_average = 2.3

# Initialize MrE model
mre = MaximumRelativeEntropy(data, expected_average)

# Run model
posterior_distribution = mre.update()

# Display results
print("Posterior Distribution:")
print(posterior_distribution)

# Save results to CSV
posterior_distribution.to_csv('results/posterior_distribution.csv', index=False)  
print("\nResults saved to 'results/posterior_distribution.csv'")
