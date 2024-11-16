# Yield Curve Construction and Analysis

## Overview
This project focuses on constructing yield curves using various models such as the Nelson-Siegel, Nelson-Siegel-Svensson, and cubic spline interpolation. Additionally, it includes the analysis of macroeconomic impacts on the yield curve and the calculation of bond portfolio metrics like zero-coupon yields, forward rates, and durations.

## Project Structure
- **src/**: Contains Python scripts for different yield curve models and metric calculations.
- **data/**: A folder for input data such as historical yield and macroeconomic data.
- **notebooks/**: Jupyter notebooks for running interactive analyses.
- **visuals/**: Stores plots and other visual outputs.

## Key Features
- **Yield Curve Construction**:
  - **Nelson-Siegel Model**: Parameterized representation of the yield curve.
  - **Nelson-Siegel-Svensson Model**: Extension of Nelson-Siegel for more flexibility.
  - **Cubic Spline Interpolation**: Smooth curve fitting between data points.
- **Macroeconomic Analysis**:
  - Correlation between inflation, monetary policy, and yield curve shifts.
- **Bond Portfolio Metrics**:
  - Zero-coupon yield calculation using bootstrapping.
  - Forward rate estimation.
  - Bond duration for risk management.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Shecd4fn/yield-curve-construction-analysis.git
   cd yield-curve-construction-analysis

