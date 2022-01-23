# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

def rivers_with_station(stations):
    """Build and return a set of all rivers with at least one station."""
    
    rivers = set()
    for station in stations:
        rivers.add(station.river)
    

    return rivers
