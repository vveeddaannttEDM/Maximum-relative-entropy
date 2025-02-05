import numpy as np
import pandas as pd
from scipy.optimize import minimize

class MaximumRelativeEntropy:
    def __init__(self, data, expected_average):
        self.data = data
        self.expected_average = expected_average
        self.types = data.columns.tolist()
        self.sample_counts = data.sum(axis=0).values
        self.total_samples = self.sample_counts.sum()
        
    def entropy(self, probabilities):
        return -np.sum(probabilities * np.log(probabilities))

    def constraint(self, probabilities):
        return np.dot(probabilities, range(1, len(probabilities) + 1)) - self.expected_average

    def update(self):
        k = len(self.types)
        initial_prob = np.ones(k) / k  # Start with uniform distribution
        
        # Constraints: sum to 1 and match expected average
        constraints = (
            {'type': 'eq', 'fun': lambda p: np.sum(p) - 1},
            {'type': 'eq', 'fun': self.constraint}
        )
        
        # Bounds: probabilities between 0 and 1
        bounds = [(0, 1) for _ in range(k)]
        
        # Minimize negative entropy
        result = minimize(lambda p: -self.entropy(p), initial_prob, bounds=bounds, constraints=constraints)
        
        if result.success:
            posterior_probs = result.x
            return pd.DataFrame({"Type": self.types, "Probability": posterior_probs})
        else:
            raise ValueError("Optimization failed: " + result.message)
