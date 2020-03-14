let map = L.map('map').setView([-33.584491, -70.676733],13)

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
	attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);



L.Routing.control({
    waypoints: [
		L.latLng(-33.574758, -70.675552),
		L.latLng(-33.575946, -70.668014),
		L.latLng(-33.582300, -70.689205),
		L.latLng(-33.561528, -70.676688),
		L.latLng(-33.565860, -70.671914),
		L.latLng(-33.560894, -70.657658),
		L.latLng(-33.571703, -70.665466),
		L.latLng(-33.576958, -70.690707),
		L.latLng(-33.591874, -70.671005),
		L.latLng(-33.597625, -70.690105)
	],
	

}).addTo(map);
console.log("QASAS");
/*
var control = L.Routing.control(L.extend(window.lrmConfig, {
    waypoints: [
		L.latLng(-33.574758, -70.675552),
		L.latLng(-33.575946, -70.668014),
		L.latLng(-33.582300, -70.689205),
		L.latLng(-33.561528, -70.676688),
		L.latLng(-33.565860, -70.671914),
		L.latLng(-33.560894, -70.657658),
		L.latLng(-33.571703, -70.665466),
		L.latLng(-33.576958, -70.690707),
		L.latLng(-33.591874, -70.671005),
		L.latLng(-33.597625, -70.690105)
	],

	geocoder: L.Control.Geocoder.nominatim(),
	routeWhileDragging: true,
	reverseWaypoints: true,
	showAlternatives: true,
	altLineOptions: {
		styles: [
			{color: 'black', opacity: 0.15, weight: 9},
			{color: 'white', opacity: 0.8, weight: 6},
			{color: 'blue', opacity: 0.5, weight: 2}
		]
	}
})).addTo(map);
*/
//L.Routing.errorControl(control).addTo(map);

