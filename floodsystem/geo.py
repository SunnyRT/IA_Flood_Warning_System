# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

# edited by lrl35
"""This module contains a collection of functions related to
geographical data.

"""
from station import MonitoringStation
from stationdata import build_station_list
from utils import sorted_by_key  # noqa
from haversine import haversine, Unit

def stations_by_distance(stations, p):
    """Function to return a sorted list of (station, distance) tuple by distance (kilometres) from coordinate p."""
    stationlist = []
    for i in stations:
        dist = haversine(i.coord , p)
        stationtuple = (i.name, dist)
        stationlist.append(stationtuple)
    sortedstations = sorted_by_key(stationlist, 1, reverse=False)
    return sortedstations
