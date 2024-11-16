
import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

def cubic_spline_interpolation(maturities_points, yields_points, maturities_fine):
    """
    Interpolates yield data using cubic spline interpolation.
    
    Parameters:
    maturities_points : array-like : The maturities at which yield data points are known.
    yields_points : array-like : The yield values at the given maturities.
    maturities_fine : array-like : The maturities at which to evaluate the interpolated yields.
    
    Returns:
    array : Interpolated yields at the specified fine maturities.
    """
    # Create a cubic spline interpolation function
    cs = CubicSpline(maturities_points, yields_points)
    
    # Evaluate the cubic spline at the specified fine maturities
    yields_interpolated = cs(maturities_fine)
    
    return yields_interpolated

def plot_cubic_spline(maturities_points, yields_points, maturities_fine, yields_interpolated):
    """
    Plots the cubic spline interpolation along with the original data points.
    
    Parameters:
    maturities_points : array-like : The maturities at which yield data points are known.
    yields_points : array-like : The yield values at the given maturities.
    maturities_fine : array-like : The maturities at wh

