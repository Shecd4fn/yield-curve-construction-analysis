import numpy as np
def zero_coupon_yield(par_yields, maturities):
    """
    Calculate zero-coupon yields from par yields using bootstrapping.

    Parameters:
    par_yields : array : Par yields for corresponding maturities.
    maturities : array : Maturities in years.

    Returns:
    array : Zero-coupon yields.
    """
    zero_coupon_rates = np.zeros(len(par_yields))
    for i in range(len(par_yields)):
        if i == 0:
            zero_coupon_rates[i] = par_yields[i]
        else:
            sum_discounted_cashflows = sum(par_yields[i] / (1 + zero_coupon_rates[j])**maturities[j] for j in range(i))
            zero_coupon_rates[i] = ((1 + par_yields[i]) / (1 - sum_discounted_cashflows))**(1 / maturities[i]) - 1
    return zero_coupon_rates

# Example usage
par_yields = np.array([0.02, 0.025, 0.03, 0.035, 0.04, 0.045])
zero_yields = zero_coupon_yield(par_yields, maturities_points)
