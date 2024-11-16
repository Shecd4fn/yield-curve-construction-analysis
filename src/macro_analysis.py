import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

def analyze_macroeconomic_impact(macro_data, yield_data):
    """
    Analyzes the correlation between macroeconomic data and yield curve data.
    
    Parameters:
    macro_data : pd.Series : A time series of macroeconomic data (e.g., inflation, interest rates).
    yield_data : pd.Series : A time series of yield curve data (e.g., yields at specific maturities).

    Returns:
    float : The correlation coefficient between macroeconomic data and yield data.
    """
    # Ensure the data are aligned in terms of time
    aligned_data = pd.concat([macro_data, yield_data], axis=1).dropna()
    aligned_data.columns = ['Macro', 'Yield']

    # Check if aligned_data is empty
    if aligned_data.empty:
        print("Aligned data is empty after concatenation. Check if your input series have matching indices.")
        return None

    # Calculate correlation
    correlation, _ = pearsonr(aligned_data['Macro'], aligned_data['Yield'])
    
    # Plotting the relationship
    plt.figure(figsize=(10, 6))
    plt.scatter(aligned_data['Macro'], aligned_data['Yield'], alpha=0.6)
    plt.title('Macroeconomic Data vs Yield Curve Data')
    plt.xlabel('Macroeconomic Variable')
    plt.ylabel('Yield')
    plt.grid(True)
    plt.show()

    print(f'Correlation between macroeconomic data and yield data: {correlation:.2f}')
    
    return correlation
