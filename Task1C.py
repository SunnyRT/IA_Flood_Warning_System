# lrl35

from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for 1C"""
    # Create station list and call function
    stations = build_station_list()
    radialstations = stations_within_radius(stations, (52.2053, 0.1218), 10)
    # Create a blank list and fill with the names of stations within radius
    radstationslist = []
    for i in radialstations:
        radstationslist.append(i.name)
    # Make alphabetical
    radstationslist.sort()
    return print(radstationslist)

if __name__ == "__main__":
    run()