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



def forward_rate(zero_rates, maturities):
    """
    Calculate forward rates between periods.

    Parameters:
    zero_rates : array : Zero-coupon rates.
    maturities : array : Maturities in years.

    Returns:
    array : Forward rates between periods.
    """
    forward_rates = []
    for i in range(1, len(zero_rates)):
        rate = ((1 + zero_rates[i])**maturities[i] / (1 + zero_rates[i - 1])**maturities[i - 1])**(1 / (maturities[i] - maturities[i - 1])) - 1
        forward_rates.append(rate)
    return np.array(forward_rates)



def macaulay_duration(cashflows, discount_rates, periods):
    """
    Calculate the Macaulay duration of a bond.

    Parameters:
    cashflows : array : Cashflows of the bond.
    discount_rates : array : Discount rates for each period.
    periods : array : Periods in years for each cashflow.

    Returns:
    float : Macaulay duration.
    """
    discounted_cashflows = cashflows / (1 + discount_rates)**periods
    weighted_average = np.sum(periods * discounted_cashflows) / np.sum(discounted_cashflows)
    return weighted_average



