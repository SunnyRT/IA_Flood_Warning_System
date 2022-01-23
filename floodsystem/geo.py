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

def stations_by_river(stations):
    """Build and return a dictionary that maps river names to 
    a list of station objects on a given river.
    """
    rivers = rivers_with_station(stations)

    river_stations_dict = {river:[] for river in list(rivers)}
    for station in stations:
        station_list = river_stations_dict[station.river]
        station_list.append(station.name)

    # For each river, sort its list of stations.
    for item in river_stations_dict.values():
        item.sort()

    return river_stations_dict


def rivers_by_station_number(stations, N):
    """Build and return a list containing the N rivers 
    with the greatest number of monitoring stations."""
    
    dict = stations_by_river(stations)


    # Build a list of tuples containting each river with the number of its stations.
    station_number_list = [(river, len(dict[river])) for river in dict.keys()]

    # Sort the list of river by its number of stations in descending order.
    sorted_list = sorted(station_number_list, key=lambda tup: tup[1], reverse=True)

    # Identify and retrieve the first N rivers (with greastest number of stations) in the sorted list.
    # If consider only the last entry rivers with same number of stations.
    max_list = sorted_list[:N]
    
    for i in range(N, len(sorted_list)):
        if sorted_list[i][1] == max_list[-1][1]:
            max_list.append(sorted_list[i])
        else:
            break

    # If consider all rivers with same number of stations.
    """ 
    n = 0
    max_list = [sorted_list[0]]
    for i in range(1,len(sorted_list)):
        if n >= N-1:
            break
        elif sorted_list[i][1] != sorted_list[i-1][1] and n < N-1:
            max_list.append(sorted_list[i])
            n += 1
        else:
            max_list.append(sorted_list[i]) 
    """


    return max_list




    
