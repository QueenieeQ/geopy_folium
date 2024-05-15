const correctProvince = 'Hà Nội';

function handleProvinceSelection(provinceName) {
  if (provinceName === correctProvince) {
    celebrate(); // Celebrate if correct province selected
  } else {
    showIncorrectMessage(); // Notify user to try again if incorrect province
  }
}

function celebrate() {
  alert('Congratulations! You found Hanoi!');
}

function showIncorrectMessage() {
  alert('Incorrect province. Please try again.');
}

var geo_json_3f3c21fa95848281d4ace70cb3d78556 = L.geoJson(null, {
  onEachFeature: function(feature, layer) {
    layer.on({
      click: function(e) {
        const provinceName = e.target.feature.properties.name;
        handleProvinceSelection(provinceName);
      },
      mouseout: function(e) {
        if (typeof e.target.setStyle === "function") {
          geo_json_3f3c21fa95848281d4ace70cb3d78556.resetStyle(e.target);
        }
      },
      mouseover: function(e) {
        if (typeof e.target.setStyle === "function") {
          const highlightStyle = geo_json_3f3c21fa95848281d4ace70cb3d78556_highlighter(e.target.feature);
          e.target.setStyle(highlightStyle);
        }
      },
    });
  },
  style: geo_json_3f3c21fa95848281d4ace70cb3d78556_styler,
});

// ... rest of your code for adding GeoJSON data and styling

// Add GeoJSON layer for province borders with click event listener
L.geoJson(provinceData, {
    onEachFeature: function (feature, layer) {
        layer.on({
            click: onProvinceClick // Attach click event listener to each province
        });
    }
}).addTo(map);
