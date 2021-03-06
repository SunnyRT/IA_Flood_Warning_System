# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    # addition of task 1F
    def typical_range_consistent(self):
        """Checks for consistency in high/low range data"""
        if type(self.typical_range) != tuple:
            return False
        if self.typical_range[1] - self.typical_range[0] > 0:
            if type(self.typical_range[1] - self.typical_range[0]) == float:
                return True
        else:
            return False

    # addition of task 2B
    def relative_water_level(self):
        """Return the latest water level as a function of the typical range.
        i.e. a ratio of 1.0 corresponds to a level at the typical high
        and a ratio of 0.0 corresponds to a level at the typical low."""
        if self.typical_range_consistent() == True:
            if type(self.latest_level) == float:
                numerator = self.latest_level - self.typical_range[0]
                denominator = self.typical_range[1] - self.typical_range[0]
                ratio = numerator / denominator
                # finds relative level by finding how far into the range
                return ratio
        else:
            return None


# addition of task 1F
def inconsistent_typical_range_stations(stations):
    """Given list of stations, returns list of stations with inconsistent data"""
    inconsiststations = []
    for i in stations:
        if i.typical_range_consistent() == False:
            inconsiststations.append(i)
    return inconsiststations

