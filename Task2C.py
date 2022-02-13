"""For Task 2C"""

from floodsystem.flood import stations_highest_rel_level
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)
    stationlist = stations_highest_rel_level(stations, 10)
    for i in stationlist:
        print(i)

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
    print("There is a limit of 500 for relative levels. Beyond 500 is conisdered inconsistent.")