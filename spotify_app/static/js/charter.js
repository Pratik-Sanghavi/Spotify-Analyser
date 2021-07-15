var ctx = document.getElementsByClassName("chartjs-gauge-dance");
make_chart(ctx, danceability, 1);
var ctx = document.getElementsByClassName("chartjs-gauge-energy");
make_chart(ctx, energy, 1);
var ctx = document.getElementsByClassName("chartjs-gauge-key");
make_chart(ctx, key_mean, key_max);
var ctx = document.getElementsByClassName("chartjs-gauge-speech");
make_chart(ctx, speech, 1);
var ctx = document.getElementsByClassName("chartjs-gauge-acoustic");
make_chart(ctx, acoustic, 1);
var ctx = document.getElementsByClassName("chartjs-gauge-instrument");
make_chart(ctx, instrument_mean, instrument_max);
var ctx = document.getElementsByClassName("chartjs-gauge-live");
make_chart(ctx, live, 1);
var ctx = document.getElementsByClassName("chartjs-gauge-valence");
make_chart(ctx, valence, 1);
var ctx = document.getElementsByClassName("chartjs-gauge-tempo");
make_chart(ctx, tempo_mean, tempo_max);

function make_chart(ctx, var_mean, var_max){
    
    const score = parseFloat(var_mean);
    const max_score = parseFloat(var_max);
    if(Math.round(score*100)/100!=0)
    {
        var dat = [Math.round(score*100)/100, (Math.round((var_max - score)*100)/100)]
    }
    else
    {
        var dat = [score, var_max - score]
    }
    var chart = new Chart(ctx, {
        type:"doughnut",
        data: {
            labels : ["",""],
            datasets: [{
                label: "Meter",
                data : dat,
                backgroundColor: [
                    "rgb(255, 99, 132)",
                    "rgb(54, 162, 235)",
                    "rgb(255, 205, 86)"
                ]
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            circumference: Math.PI,
            rotation : Math.PI,
            cutoutPercentage : 80,
            legend: {
                display: false
            },
            tooltips: {
                enabled: true
            }
        }
    });
    return;
}