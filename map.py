import folium
from geopy.geocoders import Nominatim

# Initialize a geocoder
geolocator = Nominatim(user_agent="my_geocoder")

# Get coordinates for a location (e.g., Hanoi, Vietnam)
location = geolocator.geocode("Hanoi, Vietnam")

# Create a Folium map centered around the location
m = folium.Map(location=[location.latitude, location.longitude], zoom_start=6)

# Load GeoJSON data for Vietnam's provinces
with open('diaphantinh.geojson') as f:
    province_data = f.read()

# Add GeoJSON layer for province borders
folium.GeoJson(province_data, name='province borders').add_to(m)

# Add a marker for the location
folium.Marker([location.latitude, location.longitude], popup="Hanoi, Vietnam").add_to(m)

# Save the map to an HTML file and open it in a web browser
m.save('vietnam_map_with_provinces.html')
