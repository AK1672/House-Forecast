function toggleFeatures() {
    var additionalFeatures = document.getElementById("additionalFeatures");
    if (additionalFeatures.classList.contains("hidden")) {
      document.getElementById("f1").style.width = "850px";
      document.getElementById("f1").style.height = "400px";
      setTimeout(function() {
        additionalFeatures.classList.remove("hidden");
    }, 320);
      
    } else {
      document.getElementById("f1").style.width = "400px";
      document.getElementById("f1").style.height = "350px";
      additionalFeatures.classList.add("hidden");
    }
  }


  var platform = new H.service.Platform({
    'apikey': 'REpw-l9BNWxK9B1nrLkAAKiJCcRI4bnX_3KHcz1XAjg'
  });

  // Obtain the default map types from the platform object:
var defaultLayers = platform.createDefaultLayers();

// Instantiate (and display) a map object:
var map = new H.Map(
    document.getElementById('mapContainer'),
    defaultLayers.vector.normal.map,
    {
      zoom: 10,
      center: { lat:28.6139, lng:77.2088 }
    });
    lt=parseFloat(document.getElementById("lat").value);
    ln=parseFloat(document.getElementById("lng").value);
      var pMarker = new H.map.Marker({lat:lt, lng:ln });
      map.addObject(pMarker);
      map.setCenter(pMarker.getGeometry());

