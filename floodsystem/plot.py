import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib
from floodsystem.analysis import polyfit

def plot_water_levels(station, dates, levels):
    """Displays a plot of the water level data against time for a station, 
    also include on the plot lines for the typical low and high levels."""

    t = dates
    level = levels
    plt.plot(t, level)

    # Plot typical range low/high
    typical_range = station.typical_range
    low_level = float(typical_range[0])
    high_level = float(typical_range[1])
    plt.hlines(low_level, min(t), max(t), 'g', '-.')
    plt.hlines(high_level, min(t), max(t), 'g', '-.')

    plt.xlabel("date")
    plt.ylabel("water level(m)")
    plt.xticks(rotation=45)
    plt.title(station)

    plt.tight_layout()
    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):

    x = matplotlib.dates.date2num(dates)
    y = levels
    # Obtain the fitting polynomial ploy and shift of date (time) axis d0.
    poly, d0 = polyfit(dates, levels, p)
    
    # Plot original data points
    plt.plot(dates, y, '.')

    # Plot polynomial fit 
    # Polynomial is evaluated using the shift x)
    plt.plot(dates, poly(x-d0))

    # Plot typical range low/high
    typical_range = station.typical_range
    low_level = float(typical_range[0])
    high_level = float(typical_range[1])
    plt.hlines(low_level, min(x), max(x), 'g', '-.')
    plt.hlines(high_level, min(x), max(x), 'g', '-.')

    plt.xlabel("date")
    plt.ylabel("water level(m)")
    plt.xticks(rotation=45)
    plt.title(station)

    # Display plot
    plt.tight_layout()
    plt.show()
    
    return poly(x-d0)
