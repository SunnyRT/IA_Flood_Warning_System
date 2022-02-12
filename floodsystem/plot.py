import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from datafetcher import fetch_measure_levels

def plot_water_levels(station, dates, levels):
    t = dates
    level = levels
    plt.plot(t, level)

    plt.xlabel("date")
    plt.ylabel("water level(m)")
    plt.xticks(rotation=45);
    plt.title("Water Levels at Station {}".format(station))

    plt.tight_layout()
    plt.show()