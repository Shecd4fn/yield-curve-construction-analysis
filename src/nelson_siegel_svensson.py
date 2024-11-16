import numpy as np

def nelson_siegel_svensson(t, beta0, beta1, beta2, beta3, tau1, tau2):
    """
    Nelson-Siegel-Svensson yield curve model.
    
    Parameters:
    t : array : Array of maturities.
    beta0, beta1, beta2, beta3 : floats : Model parameters.
    tau1, tau2 : floats : Decay factors.
    
    Returns:
    array : Yields for given maturities.
    """
    term1 = beta0
    term2 = beta1 * (1 - np.exp(-t / tau1)) / (t / tau1)
    term3 = beta2 * ((1 - np.exp(-t / tau1)) / (t / tau1) - np.exp(-t / tau1))
    term4 = beta3 * ((1 - np.exp(-t / tau2)) / (t / tau2) - np.exp(-t / tau2))
    return term1 + term2 + term3 + term4

# Example usage
yields_svensson = nelson_siegel_svensson(maturities, beta0=0.03, beta1=-0.02, beta2=0.02, beta3=0.01, tau1=2.0, tau2=0.5)
