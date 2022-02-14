import matplotlib
import numpy as np
import matplotlib.pyplot as plt


def polyfit(dates, levels, p):
    """Compute a least-squares fit of a polynomial of degree p to water level data,
    given the water level time history (dates, levels) for a station."""
    # Create set of data points
    x = matplotlib.dates.date2num(dates)
    y = levels

    # Find coefficients of best-fit polynomial f(x) of degree 4
    # Using shifted x values
    p_coeff = np.polyfit(x - x[0], y, 4)

    # Convert coefficient into a polynomial that can be evaluated.
    poly = np.poly1d(p_coeff)

    d0 = x[0]

    return poly, d0
    
