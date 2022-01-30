# lrl35
from floodsystem.stationdata import build_station_list

stations = build_station_list()
sing = stations[0]
print(sing)
print(type(sing.typical_range))
sing.typical_range_consistent()
print(sing.typical_range_consistent())
print(sing.typical_range[0])