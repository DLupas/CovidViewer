// google.charts.load('current', {
//     'packages':['geochart'],
//     'mapsApiKey': 'AIzaSyAZusPDjaIShqJ9Sz1os5tUzflBo_zppxQ'
// });
// google.charts.setOnLoadCallback(drawRegionsMap);

// function drawRegionsMap() {
//     var data = google.visualization.arrayToDataTable([
//     ['Province',   'Hospitals'],
//     ['CA-ON', 360],
//     ['CA-NL', 3],
//     ['CA-PE', 23],
//     ['CA-NS', 36],
//     ['CA-NB', 6],
//     ['CA-AB', 5],
//     ['CA-QC', 230],
//     ['CA-BC', 7],
//     ['CA-YT', 82],
//     ['CA-MB', 33],
//     ['CA-NT', 136],
//     ['CA-NU', 236],
//     ['CA-SK', 536],
//     ]);

//     var options = {
//     region: 'CA', // Canada
//     resolution: 'provinces',
//     colorAxis: {colors: ['#DE3163', '#880808']}, //https://htmlcolorcodes.com/colors/shades-of-red/
//     backgroundColor: '#81d4fa',
//     };

//     var chart = new google.visualization.GeoChart(document.getElementById('geochart-colors'));
//     chart.draw(data, options);
// };