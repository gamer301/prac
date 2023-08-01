import numpy as np

# Generating random data for two variables (replace these with your actual data)
np.random.seed(42)
dataset1 = np.random.rand(100) # generate 1 d random aray of 100 elem 
dataset2 = 2 * dataset1 + 1 + 0.1 * np.random.randn(100) # Simulating linear relationship with some noise


# Calculate Pearson&#39;s correlation coefficient
def pearson_correlation(x, y):
  mean_x = np.mean(x)
  mean_y = np.mean(y)
  numerator = np.sum((x - mean_x) * (y - mean_y))
  denominator = np.sqrt(np.sum((x - mean_x)**2) * np.sum((y - mean_y)**2))
  correlation_coefficient = numerator / denominator
  return correlation_coefficient

correlation_coefficient = pearson_correlation(dataset1, dataset2)

print("Ds1", dataset1)
print("Ds2", dataset2)
print("correlation", correlation_coefficient)