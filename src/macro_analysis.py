# Example: Correlation analysis between macroeconomic variables and yields
import pandas as pd

# Sample data: Replace with actual data loading
inflation_data = pd.Series(np.random.randn(100) * 0.01 + 0.02)  # Simulated inflation data
yield_curve_data = pd.Series(yields)  # Use calculated yields or actual data

correlation = inflation_data.corr(yield_curve_data)
print(f"Correlation between inflation and yield curve: {correlation:.2f}")
