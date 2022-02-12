import datetime
from floodsystem.stationdata import build_station_list, update_water_levels

from floodsystem.plot import build_water_level_dict


def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Sort the stations in list by latest water level
    data = build_water_level_dict(stations)

    print(data)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()