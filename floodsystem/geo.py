# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

# edited by lrl35
"""This module contains a collection of functions related to
geographical data.

"""
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
