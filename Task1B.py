# lrl35
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    """Requirement for Task 1B"""
    # Setting up stations sorted from (52.2053, 0.1218)
    stations = build_station_list()
    sortedstations = stations_by_distance(stations, (52.2053, 0.1218))

# NEAREST 10
    # Create new list of tuples that includes town, from sorted stations
    stattowndist = []
    # For each of the nearest 10 stations, find the appropriate town
    for i in sortedstations[:10]:
        for j in stations:
            if i[0] == j.name:
                # Set up tuple in correct order
                sttodituple = (i[0], j.town, i[1])
                stattowndist.append(sttodituple)
    print("The closest stations from the Cambridge City centre are:\n{}".format(stattowndist))

# FURTHER 10
    # Create new list of tuples that includes town, from sorted stations
    stattowndist = []
    # For each of the furthest 10 stations, find the appropriate town
    for i in sortedstations[-10:]:
        for j in stations:
            if i[0] == j.name:
                # Set up tuple in correct order
                sttodituple = (i[0], j.town, i[1])
                stattowndist.append(sttodituple)
    print("The furthest stations from the Cambridge City centre are:\n{}".format(stattowndist))

if __name__ == "__main__":
    run()