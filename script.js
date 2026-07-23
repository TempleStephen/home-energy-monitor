setInterval(function(){

let power=Math.floor(Math.random()*300)+500;

let voltage=Math.floor(Math.random()*15)+220;

let current=(power/voltage).toFixed(2);

let daily=(Math.random()*3+7).toFixed(2);

document.getElementById("power").innerHTML=power+" W";

document.getElementById("voltage").innerHTML=voltage+" V";

document.getElementById("current").innerHTML=current+" A";

document.getElementById("daily").innerHTML=daily+" kWh";

if(power>700){

document.getElementById("status").innerHTML="HIGH USAGE";

document.getElementById("status").className="warning";

}else{

document.getElementById("status").innerHTML="NORMAL";

document.getElementById("status").className="good";

}

},3000);