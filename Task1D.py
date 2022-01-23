from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = build_station_list()

    # Build set of rivers with stations
    rivers = rivers_with_station(stations)
    
    print (len(rivers), " rivers have at least one station.")
    
    print ("First 10 stations are: ", sorted(list(rivers))[:10])

            

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()