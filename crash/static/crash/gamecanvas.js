canvas = document.getElementById('chart');
ctx = canvas.getContext("2d");
ctx.font = '48px serif'
ctx.textAlign = "center"
var width = canvas.width;
var height = canvas.height;


//loads script when page loads
window.onload = function () {
    console.log(canvas, ctx)
    ctx.fillStyle = "coral"
    ctx.fillText("Welcome to Crash!", width / 2, height / 2)
    ctx.fillText("Place your bet below", width / 2, (height / 2) + 50)
};

//gets called when game_msg isWinner attribute is not None
function startGame() {
    var gameinfo = document.getElementById("gscript").getAttribute("game_info");
    console.log(gameinfo); //TESTING
    var g_dict = JSON.parse(gameinfo.replace(/'/g, '"').toLowerCase());
    var iswinner = g_dict.iswinner
    console.log(g_dict)
    animate(g_dict.crash_multiplier, 100, g_dict.iswinner, g_dict.multiplier, [0, 600])
    
}

function animate(multi, i, isWinner,cashout) {
    if (i < multi * 100) {
        i++;
        ctx.clearRect(0, 0, width, height)
        display_multiplier(i)
        display_chart(i, multi)
        setTimeout(function () {
            animate(multi, i, isWinner, cashout)
        }, 100 / (i / 100));
    }
    if (i >= multi * 100 || i > cashout * 100) {
        if (isWinner == "true") {
            ctx.fillStyle = "green"
            ctx.fillText("YOU WIN!", width / 2, (height / 2) + 50)
        } else {
            ctx.fillStyle = "red"
            ctx.fillText("The Multiplier Crashed :(", width / 2, (height / 2) + 50)
        }
        document.getElementById("infocard").setAttribute("style", "visibility:visible")
    }
    
}

function display_multiplier(i) {
    ctx.fillStyle = "black"
    var multi = i/100
    ctx.fillText(String(multi.toFixed(2))+"x",width/2,height/2)
}
function display_chart(i) {
    speed = 20*i / Math.pow(i,2)
    j = speed + i


    ctx.lineWidth=3,
    ctx.strokeStyle = "darkorange"
    ctx.beginPath();
    ctx.moveTo(0, height)
    ctx.quadraticCurveTo(j/8,height,j/4,height-(j/5))
    ctx.stroke()
}
