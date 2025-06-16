import folium

def create_map_with_markers(stations: list, 
                          map_title: str = "Location Map",
                          marker_popup: bool = True,
                          save_path: str = "map.html") -> folium.Map:
    
    if not stations:
        raise ValueError("At least one location must be provided")
    
    # Calculate the center point and bounds
    lats = [station['geo_lat'] for station in stations]
    lons = [station['geo_long'] for station in stations]
    
    center_lat = sum(lats) / len(lats)
    center_lon = sum(lons) / len(lons)
    
    # Create the base map centered on the average coordinates
    m = folium.Map(location=[center_lat, center_lon])
    
    # Add markers for each location
    for station in stations:
        lat = station['geo_lat']
        lon = station['geo_long']
        
        station_name = station.get('name', 'Unknown')
        if not lat or not lon:
            continue
        popup_text = f"{station_name}<br>Lat: {lat}<br>Lon: {lon}" if marker_popup else None
        folium.Marker(
            location=[lat, lon],
            popup=popup_text,
            tooltip=station_name
        ).add_to(m)

    
    # Fit the map to show all markers
    if len(stations) > 1:
        m.fit_bounds([[min(lats), min(lons)], [max(lats), max(lons)]])
    
    # Save the map
    m.save(save_path)
    
    return m
