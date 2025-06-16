import json

from pyradios import RadioBrowser

from station_mapping import create_map_with_markers


rb = RadioBrowser()
results = rb.stations()
print(f"Found {len(results)} stations")

results = [station for station in results if station.get('countrycode') == 'PT']
print(f"Filtered to {len(results)} stations in France")

results = [station for station in results if station.get('geo_lat') and station.get('geo_long')]
print(f"Filtered to {len(results)} stations with geographic coordinates")

create_map_with_markers(
    results,
    map_title="Radio Stations",
    marker_popup=True,
    save_path="radio_stations_map.html"
)



