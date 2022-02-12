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



def build_relative_level_dict(stations):
    """Constuct a dictionary with station name as the KEY 
    and current water level as the VALUE"""

    data = {}
    for station in stations:
        if station.latest_level != None:
            data[station.name] = station.latest_level
    
    # Sort the dictionary based on the water level 
    sorted_data = {}
    sorted_keys = sorted(data, key=data.get)  
    
    for i in sorted_keys:
        sorted_data[i] = data[i]
    
    return sorted_data

