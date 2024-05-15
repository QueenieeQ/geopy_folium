import folium
from geopy.geocoders import Nominatim

# Initialize a geocoder
geolocator = Nominatim(user_agent="my_geocoder")

# Get coordinates for a location (e.g., Hanoi, Vietnam)
location = geolocator.geocode("Hanoi, Vietnam")

# Create a Folium map centered around the location
m = folium.Map(location=[location.latitude, location.longitude], zoom_start=6,tiles="cartodb positron")

# Load GeoJSON data for Vietnam's provinces
with open('diaphantinh.geojson') as f:
    province_data = f.read()

# Define a style function to customize the appearance of the GeoJSON features
def style_function(feature):
    return {
        'color': '#989388',        # Border color
        'weight': 1,            # Line width (thinner)
        'fillColor': '#F0E4BC',
        'fillOpacity': 0.1,     # Fill opacity
    }

# Add GeoJSON layer for province borders
folium.GeoJson(province_data, name='province borders',style_function=style_function).add_to(m)

# Add a marker for the location
folium.Marker([location.latitude, location.longitude], popup="Hanoi, Vietnam").add_to(m)

folium.TileLayer('cartodb positron', opacity=0.5).add_to(m)

# Save the map to an HTML file and open it in a web browser
m.save('vietnam_map_with_provinces.html')
