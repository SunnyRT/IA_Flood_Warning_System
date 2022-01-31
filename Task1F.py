# lrl35
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations

def run():
    """Requirements for Task 1F"""
    stations = build_station_list()
    inconsistentstations = inconsistent_typical_range_stations(stations)
    inconstations = []
    for i in inconsistentstations:
        inconstations.append(i.name)
    inconstations.sort()
    return print("All the stations with inconsistent typical range date are:\n{}".format(inconstations))

if __name__ == "__main__":
    run()