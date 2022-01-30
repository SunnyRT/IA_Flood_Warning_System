from floodsystem.geo import rivers_by_station_number, rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1E"""

    # Build list of stations
    stations = build_station_list()

    # Build set of rivers with stations
    rivers = rivers_with_station(stations)

    print("List of 9 rivers with most monitoring stations: ", rivers_by_station_number(stations, 9))


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
