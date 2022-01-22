# edited by lrl35
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key  # noqa
from haversine import haversine, Unit

stationlist = build_station_list()
stationlist.append(stations.name, stations.coord)
stationlist[:3]