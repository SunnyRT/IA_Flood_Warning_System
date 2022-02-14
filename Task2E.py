import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels


def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Get the list of 5 stations with highest relative water level. 
    stationlist = stations_highest_rel_level(stations, 5)
    stationlist_name = [i[0] for i in stationlist]

    # Retrieve the history data for each station in the past 10 days.
    dt = 10
    for station in stations:
        if str(station.name) in stationlist_name:
            dates, levels = fetch_measure_levels(
                station.measure_id, dt=datetime.timedelta(days=dt))

            # Plot water levels against time for each station.
            plot_water_levels(station, dates, levels)
            
    

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()