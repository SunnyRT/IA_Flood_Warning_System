"""Unit test for flood module"""
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import datetime
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
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


def test_plot_water_level_with_fit():
     s_id = "test-s-id"
     m_id = "test-m-id"
     label = "some station"
     coord = (-2.0, 4.0)
     trange = (-2.3, 3.4445)
     river = "River X"
     town = "My Town"

     s = MonitoringStation(s_id, m_id, label, coord, trange, river, town,)
     s.latest_level = 3.3

    
     dates, levels = fetch_measure_levels("http://environment.data.gov.uk/flood-monitoring/id/measures/2514-level-stage-i-15_min-mASD",
          dt=datetime.timedelta(days=2))
     
     # Create an arbitrary polynomial function of power 4
     x = np.linspace(0, 2, len(dates))
     true_p = np.poly1d([0.5, -1.5, 1, -1, 2])
     levels = true_p(x)
     # print(levels)

     levels_fit = plot_water_level_with_fit(s, dates, levels, 4)
     # print(levels_fit)

     assert len(levels) == len(levels_fit)
     difference = levels - levels_fit
     # print(difference)
     # np.testing.assert_allclose(levels_fit[0], true_p(0), rtol = 0.01)
     # np.testing.assert_allclose(levels_fit[-1], true_p(2), rtol = 0.01)
     
     for i in difference:
          assert i <= 0.01 # set error of fitting to be 1%
     