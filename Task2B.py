"""For Task 2B"""

from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)
    stationlist = stations_level_over_threshold(stations, 0.8)
    for i in stationlist:
        print(i)

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
    print("There is a limit of 500 for relative levels. Beyond 500 is conisdered inconsistent.")