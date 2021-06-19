var xmlHttp = new XMLHttpRequest();
var url = "static/pastdata.json";
xmlHttp.open("GET", url, true);
xmlHttp.send();
xmlHttp.onreadystatechange = function() {
    if(this.readyState == 4 && this.status == 200) {
        var data = JSON.parse(this.responseText);
        //console.log(data);
        var date = data.covid.map(function(elem) {
            return elem.date;
        });
        var cases = data.covid.map(function(elem) {
            return elem.cases;
        });
        var deaths = data.covid.map(function(elem) {
            return elem.deaths;
        });
        var ctx = document.getElementById('canvas').getContext('2d');
        Chart.defaults.elements.point.radius = 0;
        var myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: date,
                datasets: [{
                    label: '# of Cases',
                    data: cases,
                    backgroundColor: 'transparent',
                    borderColor:'blue' ,
                    borderWidth: 4

                },
                {
                    label: '# of Deaths',
                    data: deaths,
                    backgroundColor: 'transparent',
                    borderColor:'red' ,
                    borderWidth: 4
                }]
            },
            
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                        
                    }
                }
            }
        });
    }
}
