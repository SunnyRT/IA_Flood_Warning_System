"""This module is for Task 2B and 2C"""
from ast import Pass
from audioop import reverse
from re import X

from numpy import average
from .station import MonitoringStation
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import matplotlib
from floodsystem.analysis import polyfit

import matplotlib.pyplot as plt


def stations_level_over_threshold(stations, tol):
    """Function that returns list of tuples of stations above tolerance, and relative water level"""
    newlist = []
    for i in stations:
        if type(i.relative_water_level()) == float:
            if 500 > i.relative_water_level() > tol:
                newtuple = (i.name, i.relative_water_level())
                # creating a tuple with the name and relative
                newlist.append(newtuple)
    newlist.sort(key = lambda x: x[1], reverse = True)
    return newlist

def stations_highest_rel_level(stations, N):
    newlist = []
    for i in stations:
        if type(i.relative_water_level()) == float:
            if i.relative_water_level() < 100: 
                newtuple = (i.name, i.relative_water_level())
                newlist.append(newtuple)
            # same process as for threshold, without a threshold though
    newlist.sort(key = lambda x: x[1], reverse = True)
    return newlist[:(N)]




# Addtion for Task2G
def station_risk(station):
    """Rate the risk level of each station such that:
    0 - low, 1 - moderate, 2 - high, 3 - severe."""

    dt = 2

    # Get history data for past 2 days
    dates, levels = fetch_measure_levels(
        station.measure_id, dt=datetime.timedelta(days=dt))
    
    x = matplotlib.dates.date2num(dates)    

    # Predict future data for next 2 days
    if dates != [] and levels != []:

        poly, d0 = polyfit(dates, levels, p = 4)
        future_levels = poly(x - d0 + dt)
        combined_levels = levels + list(future_levels)


        # Determin and return risk level based on all datas
        risk = None
        
        if max(combined_levels) >= 2: # "severe" threshold
            risk_rate = 3                    # severe

        elif max(combined_levels) >= 1:
            risk_rate = 2                    # high

        elif max(combined_levels) >= 0:
            risk_rate = 1                    # moderate

        elif max(combined_levels) < 0:
            risk_rate = 0                    # low

        return (station.name, risk_rate)

    else:
        print("Data is not avaiable.")

        



def town_risk(stations):
    """Return a sorted list of top 10 towns at the greatest risks.
    Criteria: Average of past-2-day history data and next-2-day future data."""
    town_dict = {}
    dt = 2
    for station in stations:
        # Get history data for past 2 days
        dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=dt))

        if dates != [] and levels != []:
             
            # Predict future data for next 2 days
            poly, d0 = polyfit(dates, levels, p = 4)
            
            x = matplotlib.dates.date2num(dates)
            future_levels = poly(x[:10] - d0 + dt)
            combined_levels = levels + list(future_levels)

             # Compute risk index = average of past-2-day history data and next-2-day future data.
            risk_index = average(combined_levels)
            town_dict[station.town] = risk_index
            print(risk_index)

    sorted_dict = sorted(town_dict.items(), key=lambda item: item[1], reverse = True)
    return sorted_dict[:5]




'''
def town_stations_risk(stations):
    """Construct a dictionary, 
    which maps each town to a list, which indicates the number of stations 
    with risk level of "severe", "high", "moderate" and "low" respectively.
    i.e. {town_1: [0,1,2,1], town_2: [4,1,3,3], ...]"""

    town_dict = {}
    n = 0
    for station in stations:
        if station.latest_level == None:
            pass
        else:
            # Compute risk level for each station.
            r = station_risk(station)
            print(r)

            # Determine if the town is already included in the dictionary to avoid repetition
            if not station.town in town_dict.keys():
                town_dict[station.town] = [0,0,0,0]
                town_dict[station.town][r] = 1
            else:
                town_dict[station.town][r] += 1

            
    return town_dict
'''
