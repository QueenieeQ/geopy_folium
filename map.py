import folium
import json
# from folium import features
# from geopy.geocoders import Nominatim

# Initialize a geocoder
# geolocator = Nominatim(user_agent="my_geocoder")

# Get coordinates for a location (e.g., Hanoi, Vietnam)
# location = geolocator.geocode("Hanoi, Vietnam")

# Create a Folium map centered around the location
m = folium.Map(location=[15.5, 106.5], zoom_start=6,tiles="cartodb positron")

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

# Add the GeoJSON layer to the map


# Add GeoJSON layer for province borders
geojson_layer = folium.GeoJson(province_data, name='province borders',style_function=style_function).add_to(m)
geojson_layer.add_to(m)

# Add a marker for the location
# folium.Marker([location.latitude, location.longitude], popup="Hanoi, Vietnam").add_to(m)

# Define JavaScript function to handle province click events
highlight_function = """
function highlightFeature(e) {
    var layer = e.target;
    layer.setStyle({
        weight: 2,
        color: '#666',
        fillColor: 'orange', // Highlight fill color
        fillOpacity: 0.7
    });
    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
        layer.bringToFront();
    }
}

function resetHighlight(e) {
    geojson_layer.resetStyle(e.target);
}

function onEachFeature(feature, layer) {
    layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight
    });
}
"""

# Add custom JavaScript code to the map
folium.Map().add_child(folium.Element(f"""
    <script>
    {highlight_function}
    </script>
"""))

folium.TileLayer('cartodb positron', opacity=0.5).add_to(m)

# Save the map to an HTML file and open it in a web browser
m.save('vietnam_map_with_provinces.html')
