// THIS FILE WAS CREATED BY ANANTH. IT IS WAS HERE FOR TESTING AND SCRATCH WORK PURPOSES.
// NOT SUPPOSED TO BE USED TO RUN THE ACTUAL PROGRAM.

// google.charts.load('current', { 'packages':['geochart'], 'mapsApiKey': 'AIzaSyAZusPDjaIShqJ9Sz1os5tUzflBo_zppxQ'});
// google.charts.setOnLoadCallback(drawRegionsMap);
// function drawRegionsMap() {
//     var url = `{ "covid" :[
// { "province" : "CA-ON",
// "cases": 50,
// "deaths": 20 },
// {
// "province" : "CA-NL",
// "cases": 60,
// "deaths": 10
// },
// {
// "province" : "CA-PE",
// "cases": 70,
// "deaths": 5
// },
// {
// "province" : "CA-NS",
// "cases": 80,
// "deaths": 15
// },
// {
// "province" : "CA-NB",
// "cases": 60,
// "deaths": 10
// },
// {
// "province" : "CA-AB",
// "cases": 90,
// "deaths": 40
// },
// {
// "province" : "CA-QC",
// "cases": 50,
// "deaths": 20

// },
// {
// "province" : "CA-BC",
// "cases": 60,
// "deaths": 10
// },
// {
// "province" : "CA-YT",
// "cases": 70,
// "deaths": 5
// },
// {
// "province" : "CA-MB",
// "cases": 80,
// "deaths": 15
// },
// {
// "province" : "CA-NT",
// "cases": 60,
// "deaths": 10
// },
// {
// "province" : "CA-NU",
// "cases": 90,
// "deaths": 40
// },
// {
// "province" : "CA-SK",
// "cases": 90,
// "deaths": 40
// }
// ]
// }`;
//     var data1 = JSON.parse(url);
//         var province = data1.covid.map(function(elem) {
//             return elem.province;
//         });
//         var cases = data1.covid.map(function(elem) {
//             return elem.cases;
//         });
//         var deaths = data1.covid.map(function(elem) {
//             return elem.deaths;
//         });
//         var data = new google.visualization.arrayToDataTable([
//         ['Province','Cases','Deaths'],
//         [province[0], cases[0], deaths[0]],
//         [province[1], cases[1], deaths[1]],
//         [province[2], cases[2], deaths[2]],
//         [province[3], cases[3], deaths[3]],
//         [province[4], cases[4], deaths[4]],
//         [province[5], cases[5], deaths[5]],
//         [province[6], cases[6], deaths[6]],
//         [province[7], cases[7], deaths[7]],
//         [province[8], cases[8], deaths[8]],
//         [province[9], cases[9], deaths[9]],
//         [province[10], cases[10], deaths[10]],
//         [province[11], cases[11], deaths[11]],
//         [province[12], cases[12], deaths[12]],
//         ]);
//         var chart = new google.visualization.GeoChart(document.getElementById('chart_div'));
//         var options = {
//         region: 'CA', // Canada
//         resolution: 'provinces',
//         colorAxis: {colors: ['#35de35', '#1c8c1c']}, //https://htmlcolorcodes.com/colors/shades-of-red/
//         backgroundColor: '#81d4fa',
//         };
//     console.log(province);
//     chart.draw(data, options);
// };




















// var url = `{ "covid" :[
//     { "province" : "CA-ON",
//     "cases": 50,
//     "deaths": 20 },
//     {
//     "province" : "CA-NL",
//     "cases": 60,
//     "deaths": 10
//     },
//     {
//     "province" : "CA-PE",
//     "cases": 70,
//     "deaths": 5
//     },
//     {
//     "province" : "CA-NS",
//     "cases": 80,
//     "deaths": 15
//     },
//     {
//     "province" : "CA-NB",
//     "cases": 60,
//     "deaths": 10
//     },
//     {
//     "province" : "CA-AB",
//     "cases": 90,
//     "deaths": 40
//     },
//     {
//     "province" : "CA-QC",
//     "cases": 50,
//     "deaths": 20
    
//     },
//     {
//     "province" : "CA-BC",
//     "cases": 60,
//     "deaths": 10
//     },
//     {
//     "province" : "CA-YT",
//     "cases": 70,
//     "deaths": 5
//     },
//     {
//     "province" : "CA-MB",
//     "cases": 80,
//     "deaths": 15
//     },
//     {
//     "province" : "CA-NT",
//     "cases": 60,
//     "deaths": 10
//     },
//     {
//     "province" : "CA-NU",
//     "cases": 90,
//     "deaths": 40
//     },
//     {
//     "province" : "CA-SK",
//     "cases": 90,
//     "deaths": 40
//     }
//     ]
//     }`;
//         var data1 = JSON.parse(url);