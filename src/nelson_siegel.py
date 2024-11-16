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

# Example usage
maturities = np.linspace(0.1, 30, 100)  # Maturities from 0.1 to 30 years
yields = nelson_siegel(maturities, beta0=0.03, beta1=-0.02, beta2=0.02, tau=2.0)
