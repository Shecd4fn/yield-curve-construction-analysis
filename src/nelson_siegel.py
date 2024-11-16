import numpy as np

def nelson_siegel(t, beta0, beta1, beta2, tau):
    """
    Nelson-Siegel yield curve model.
    
    Parameters:
    t : array : Array of maturities.
    beta0, beta1, beta2 : floats : Model parameters.
    tau : float : Decay factor.
    
    Returns:
    array : Yields for given maturities.
    """
    term1 = beta0
    term2 = beta1 * (1 - np.exp(-t / tau)) / (t / tau)
    term3 = beta2 * ((1 - np.exp(-t / tau)) / (t / tau) - np.exp(-t / tau))
    return term1 + term2 + term3

