"""This module is for Task 2B and 2C"""
from .station import MonitoringStation

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