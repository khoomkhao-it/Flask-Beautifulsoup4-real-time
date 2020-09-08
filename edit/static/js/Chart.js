//////////////////////////////////////////////////////////////////////////////////
var lables = [[]];
var dataS = [[]];
//////////////////////////////////////////////////////////////////////////////////
function line(data,lables,target,name){//,lbales,target){
  const context = document.getElementById(target).getContext('2d');
  const config = {
    type: 'line',
    data: {
        labels: lables,
        datasets: [{
            label: name,
            backgroundColor: 'rgb(0, 99, 132)',
            borderColor: 'rgb(0, 99, 132)',
            data: data,
            fill: false,
        }],
    },
    options: {
        responsive: true,
        title: {
            display: true,
            text: ''
        },
        tooltips: {
            mode: 'index',
             intersect: false,
         },
         hover: {
            mode: 'nearest',
             intersect: true
        },
    }
  };
  const lineChart = new Chart(context, config);
}
///////////////////////////////////////////////////////////////////////////////////
function Pie(id,value,name){
  const context = document.getElementById('canvas').getContext('2d');
  const config = {
    type: 'pie',
    data: {
        labels: lables,
        datasets: [{
            label: "Random Dataset",
            backgroundColor: 'rgb(0, 99, 132)',
            borderColor: 'rgb(0, 99, 132)',
            data: data,
            fill: false,
        }],
    },
    options: {
        responsive: true,
        title: {
            display: true,
            text: 'Creating Real-Time Charts with Flask'
        },
        tooltips: {
            mode: 'index',
             intersect: false,
         },
         hover: {
            mode: 'nearest',
             intersect: true
        },
    }
  };
  const pieChart = new Chart(context, config);
}
////////////////////////////////////////////////////////////////////////////////////////////////
function Donut(id,value,name){
  const context = document.getElementById('canvas').getContext('2d');
  const config = {
    type: 'doughnut',
    data: {
        labels: lables,
        datasets: [{
            label: "Random Dataset",
            backgroundColor: 'rgb(0, 99, 132)',
            borderColor: 'rgb(0, 99, 132)',
            data: data,
            fill: false,
        }],
    },
    options: {
        responsive: true,
        title: {
            display: true,
            text: 'Creating Real-Time Charts with Flask'
        },
        tooltips: {
            mode: 'index',
             intersect: false,
         },
         hover: {
            mode: 'nearest',
             intersect: true
        },
    }
  };
  const donutChart = new Chart(context, config);
}
//////////////////////////////////////////////////////////////////////////////////////////////
/*function Area(id,value,name){
  google.charts.load('current', {'packages':['corechart']});
  google.charts.setOnLoadCallback(drawChart);

  function drawChart() {
    var data = google.visualization.arrayToDataTable([
      ['', ''],
      ['2013',  value],


    ]);

    var options = {
      title: 'Company Performance',
      'width':500,
      'height':300
    };

    var chart = new google.visualization.AreaChart(document.getElementById(id));
    chart.draw(data, options);
  }
}*/