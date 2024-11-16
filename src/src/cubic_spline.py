from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import numpy as np
# Example data for interpolation
maturities_points = np.array([1, 2, 5, 10, 20, 30])
yields_points = np.array([0.02, 0.025, 0.03, 0.035, 0.04, 0.045])

# Create a cubic spline interpolation function
cs = CubicSpline(maturities_points, yields_points)

# Interpolated yields
maturities_fine = np.linspace(0.1, 30, 300)
yields_interpolated = cs(maturities_fine)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(maturities_points, yields_points, 'o', label='Data Points')
plt.plot(maturities_fine, yields_interpolated, label='Cubic Spline Interpolation')
plt.title('Yield Curve Interpolation')
plt.xlabel('Maturity (Years)')
plt.ylabel('Yield')
plt.grid(True)
plt.legend()
plt.show()
