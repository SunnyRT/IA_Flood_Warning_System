from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = build_station_list()

    # Build set of rivers with stations
    rivers = rivers_with_station(stations)
    
    print (len(rivers), " rivers have at least one station.")
    print ("First 10 stations are: ", sorted(list(rivers))[:10])

    river_stations_dict = stations_by_river(stations)
    print ("Stations for River Aire: ", river_stations_dict["River Aire"])
    print ("Stations for River Cam: ", river_stations_dict["River Cam"])
    print ("Stations for River Thames: ", river_stations_dict["River Thames"])


            

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()