import folium
from geopy.geocoders import Nominatim

# Initialize a geocoder
geolocator = Nominatim(user_agent="my_geocoder")

# Get coordinates for a location (e.g., Hanoi, Vietnam)
location = geolocator.geocode("Hanoi, Vietnam")

# Create a Folium map centered around the location
m = folium.Map(location=[location.latitude, location.longitude], zoom_start=10)

# Add a marker for the location
folium.Marker([location.latitude, location.longitude], popup="Hanoi, Vietnam").add_to(m)

# Save the map to an HTML file and open it in a web browser
m.save('hanoi_map.html')
