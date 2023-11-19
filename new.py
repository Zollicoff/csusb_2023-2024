import numpy as np

# Step 1: Define the population
population = ['support', 'not support']
probabilities = [0.88, 0.12]

# Step 2: Draw a sample
sample = np.random.choice(population, size=1000, p=probabilities)

# Step 3: Compute the fraction of "support"
support_fraction = np.count_nonzero(sample == 'support') / len(sample)

print(f'The fraction of "support" in the sample is {support_fraction}')