from floodsystem.geo import station_coordinates
from floodsystem.stationdata import build_station_list
import plotly.graph_objects as go

def run():
    """Requirements for Milestone 1 Optional Extensions:
    Display the location of each station on a map."""

    # Build list of stations
    stations = build_station_list()

    latitudes, longitudes, texts = station_coordinates(stations)


    mapbox_access_token = open(".mapbox_token").read()

    fig = go.Figure(go.Scattermapbox(
        lat=latitudes,
        lon=longitudes,
        mode='markers',
        marker=go.scattermapbox.Marker(size=9),
        text=texts))

    fig.update_layout(autosize=True, 
        hovermode='closest',
        mapbox=dict(accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(lat=53,lon=0),
        pitch=0,
        zoom=5))
    fig.show()
    

if __name__ == "__main__":
    print("*** Optional Extensions 1: CUED Part IA Flood Warning System ***")
    run()
