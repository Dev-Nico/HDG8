var map = L.map('map').setView([0.584491, 0.676733],9)

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
	attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

L.Routing.control({
    waypoints: [/*
        L.latLng(-33.561048, -70.506516),
        L.latLng(-33.161048, -70.806516),
        L.latLng(-33.521048, -70.406516),
	*/],
	router:true,
    /*geocoder: L.Control.Geocoder.nominatim(),/*
	routeWhileDragging: true,
	/*reverseWaypoints: true,*/
	/*showAlternatives: true,*/
	waypointMode: connect,
	autoRoute: true,
	useZoomParameter:true,
	altLineOptions: {
		styles: [
			{color: 'black', opacity: 0.15, weight: 9},
			{color: 'white', opacity: 0.8, weight: 6},
			{color: 'blue', opacity: 0.5, weight: 2}
		]
	}
}).addTo(map);

L.Routing.errorControl(control).addTo(map);
