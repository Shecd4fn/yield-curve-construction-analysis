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

    # Calculate correlation
    correlation, _ = pearsonr(aligned_data['Macro'], aligned_data['Yield'])
    
    # Plotting the relatio

