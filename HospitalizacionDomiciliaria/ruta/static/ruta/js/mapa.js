let map = L.map('map').setView([-33.561048,-70.506516],11)

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
	attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

L.Routing.control({
    waypoints: [
      L.latLng(57.74, 11.94),
      L.latLng(57.6792, 11.949)
    ]
  }).addTo(map);

