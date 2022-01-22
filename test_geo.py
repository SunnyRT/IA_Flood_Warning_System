"""Unit Test for the Task 1B stations_by_distance function"""

from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

stations = build_station_list()
sortedstations = stations_by_distance(stations, (52.2053, 0.1218))
print(sortedstations[0])
print(sortedstations[5])
print(sortedstations[-1])
print(sortedstations[-5])

assert(sortedstations[0] == ('Cambridge Jesus Lock', 0.840237595667494))
assert(sortedstations[5] == ('Haslingfield Burnt Mill', 7.0443978959918025))
assert(sortedstations[-1] == ('Penberth', 467.53431870130544))
assert(sortedstations[-5] == ('St Erth', 449.0347773512542))