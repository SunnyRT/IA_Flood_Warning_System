import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def plot_water_levels(station, dates, levels):
    """Displays a plot of the water level data against time for a station, 
    also include on the plot lines for the typical low and high levels."""

    t = dates
    level = levels
    plt.plot(t, level)

    plt.xlabel("date")
    plt.ylabel("water level(m)")
    plt.xticks(rotation=45)
    plt.title(station)

    plt.tight_layout()
    plt.show()




