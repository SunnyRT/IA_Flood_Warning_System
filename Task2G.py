from floodsystem.flood import station_risk, town_risk
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from functools import reduce 

def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    print(town_risk(stations))
    

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()