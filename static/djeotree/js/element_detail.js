function map_init(map, options) {

  function onEachFeature(feature, layer) {
    if (feature.properties && feature.properties.popupContent) {
      layer.bindPopup(feature.properties.popupContent.content, {minWidth: 256});
    }
  }

  const base_map = L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
    {
      attribution: '',
      maxZoom: 19,
    }).addTo(map);

  const mapbox_token = JSON.parse(document.getElementById("mapbox_token").textContent);

  const sat_map = L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}",
    {
      attribution: 'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
      maxZoom: 19,
      tileSize: 512,
      zoomOffset: -1,
      id: "mapbox/satellite-v9",
      accessToken: mapbox_token
    });

  const baseMaps = {
    "Base": base_map,
    "Satellite": sat_map
  };
  L.control.layers(baseMaps).addTo(map);
  let collection = JSON.parse(document.getElementById("marker_data").textContent);
  let marker = L.geoJson(collection, {onEachFeature: onEachFeature});
  marker.addTo(map);
  console.log(collection)
  map.setView(
    [collection.features[0].geometry.coordinates[1],
      collection.features[0].geometry.coordinates[0]],
    19
  );
}
