var map = L.map('map').setView([-33.561048,-70.506516],11)

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
	attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

L.Routing.control({
    waypoints: [/*
        L.latLng(-33.561048, -70.506516),
        L.latLng(-33.161048, -70.806516),
        L.latLng(-33.521048, -70.406516),
    */],
    geocoder: L.Control.Geocoder.nominatim(),
    routeWhileDragging: true,
    reverseWaypoints: true,
	showAlternatives: true,
}).addTo(map);

L.Routing.errorControl(control).addTo(map);
