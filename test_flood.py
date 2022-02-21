"""Unit test for flood module"""

from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level


def test_stations_level_over_threshold():
     # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"

    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town,)
    s.latest_level = 3.3
    
    assert s.relative_water_level() == 0.9748455043955087
    
    newlist = [s]
    overthresh = stations_level_over_threshold(newlist, 0.8)

    assert overthresh == [('some station', 0.9748455043955087)]


