"""Unit Test for the Task 1B stations_by_distance function"""

from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

# STATIONS BY RADIUS TEST
def test_radius_stations():
    stations = build_station_list()
    sortedstations = stations_by_distance(stations, (52.2053, 0.1218))

    assert(sortedstations[0] == ('Cambridge Jesus Lock', 0.840237595667494))
    assert(sortedstations[5] == ('Haslingfield Burnt Mill', 7.0443978959918025))
    assert(sortedstations[-1] == ('Penberth', 467.53431870130544))
    assert(sortedstations[-5] == ('St Erth', 449.0347773512542))

# STATIONS WITHIN RADIUS TEST
# Unsure how to make a proper test, so this is an assertion of Task 1C
def test_within_radius_stations():
    stations = build_station_list()
    radialstations = stations_within_radius(stations, (52.2053, 0.1218), 10)
    radstationslist = []
    for i in radialstations:
        radstationslist.append(i.name)
    radstationslist.sort()
    assert(radstationslist == ['Bin Brook', 'Cambridge Baits Bite', "Cambridge Byron's Pool",
    'Cambridge Jesus Lock', 'Comberton', 'Dernford', 'Girton',
    'Haslingfield Burnt Mill', 'Lode', 'Oakington', 'Stapleford'])
