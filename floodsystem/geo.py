# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

# edited by lrl35
"""This module contains a collection of functions related to
geographical data.

"""
# REMEMBER TO CHANGE to .utils WHEN COMPLETE

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit

def stations_by_distance(stations, p):
    """Function to return a sorted list of (station, distance) tuple by distance (kilometres) from coordinate p."""
    # Create empty list
    stationlist = []
    for i in stations:
        # Find the distance for each station and couple it up with its name into a list of tuples
        dist = haversine(i.coord , p)
        stationtuple = (i.name, dist)
        stationlist.append(stationtuple)
    # Sort the stations by distance from p
    sortedstations = sorted_by_key(stationlist, 1, reverse=False)
    return sortedstations

def stations_within_radius(stations, centre, r):
    """Function to return a list of all stations (type MonitoringStation) within radius r of geographic coordinate x"""
    stationlist = []
    for i in stations:
        # Find distance from centre to station, if it is < r, add to list
        dist = haversine(i.coord , centre)
        if dist < r:
            stationlist.append(i)
    return stationlist
