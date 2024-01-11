import numpy as np
import matplotlib.pyplot as plt
# Generate example data
np.random.seed(0)
x = np.random.rand(50) * 10  # Example variable 1
y = 2 * x + 1 + np.random.randn(50) * 2  # Example variable 2 with linear relationship and added noise

# Create a scatterplot
plt.scatter(x, y, color='red', label='Data Points')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.title('Scatterplot of Variables X and Y')
plt.legend()
plt.grid(True)
plt.show()

# Calculate the correlation coefficient
correlation_coefficient = np.corrcoef(x, y)[0, 1]
print(f"Correlation Coefficient: {correlation_coefficient:.2f}")
