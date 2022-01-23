# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

def rivers_with_station(stations):
    """Build and return a set of all rivers 
    with at least one station."""
    
    rivers = set()
    for station in stations:
        rivers.add(station.river)
    

    return rivers

def stations_by_river(stations, rivers):
    """Build and return a dictionary that maps river names to 
    a list of station objects on a given river.
    """

    river_stations_dict = {river:[] for river in list(rivers)}
    for station in stations:
        station_list = river_stations_dict[station.river]
        station_list.append(station.name)

    # For each river, sort its list of stations.
    for item in river_stations_dict.values():
        item.sort()

    return river_stations_dict

    
