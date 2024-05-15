import folium
import json
from folium import features
from geopy.geocoders import Nominatim

# Initialize a geocoder
geolocator = Nominatim(user_agent="my_geocoder")

# Get coordinates for a location (e.g., Hanoi, Vietnam)
location = geolocator.geocode("Hanoi, Vietnam")

# Create a Folium map centered around the location
m = folium.Map(location=[location.latitude, location.longitude], zoom_start=6)

# Define the path data for the province to be highlighted
province_path = "M522 281L522 285L526 289L528 287L531 288L531 292L535 294L536 300L532 302L531 299L528 301L528 303L524 301L521 308L519 309L518 305L512 310L512 312L506 306L506 302L502 298L501 299L498 293L501 292L504 284L503 283L509 285L510 282L511 283L513 281L514 284L517 283L518 281L519 282L520 279L522 281"

# Remove the trailing character ('z') from the path data
province_path = province_path[:-1]

# Create a list of coordinates from the path data
coordinates = [tuple(map(float, point.split())) for point in province_path[1:].split("L")]

# Create a GeoJSON feature for the province with the given path data
province_feature = {
    "type": "Feature",
    "geometry": {
        "type": "Polygon",
        "coordinates": [coordinates]
    },
    "properties": {}
}

# Define a style function to customize the appearance of the GeoJSON features
def style_function(feature):
    return {
        'color': 'blue',        # Border color
        'weight': 1,            # Line width (thinner)
        'fillColor': '#F0E4BC', # Fill color in hexadecimal
        'fillOpacity': 0.5,     # Fill opacity
    }

# Add GeoJSON layer for province borders with custom styling
geojson_layer = folium.GeoJson(data={"type": "FeatureCollection", "features": [province_feature]}, name='province borders', style_function=style_function)

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

# Add a marker for the location
folium.Marker([location.latitude, location.longitude], popup="Hanoi, Vietnam").add_to(m)

# Add GeoJSON layer to the map
geojson_layer.add_to(m)

# Save the map to an HTML file and open it in a web browser
m.save('vietnam_map_with_province_highlight.html')
