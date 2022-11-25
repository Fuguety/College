const xhttp = new XMLHttpRequest();
    xhttp.onload = function () {

        requestData = JSON.parse(this.responseText);
        console.log(requestData);

    }


    


    function af(){

        //Africa Nairobi
        let latitude = '-1.2762';
        let longitude = '36.7965';
        xhttp.open("GET", `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&hourly=temperature_2m,relativehumidity_2m,rain,snowfall,cloudcover`, true);
        xhttp.send();
        console.log();

        document.getElementById("choose_city").innerHTML = "Nairobi";
    }
    
    function oc(){

        //Oceanic Canberra

        let latitude = '-35.2820';
        let longitude = '149.1286';
        xhttp.open("GET", `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&hourly=temperature_2m,relativehumidity_2m,rain,snowfall,cloudcover`, true);
        xhttp.send();
        console.log();
        
        
        document.getElementById("choose_city").innerHTML = "Canberra";


    }

    function as(){

        //Asia Tokyo

        let latitude = '35.6785';
        let longitude = '139.6823';
        xhttp.open("GET", `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&hourly=temperature_2m,relativehumidity_2m,rain,snowfall,cloudcover`, true);
        xhttp.send();
        console.log();

        document.getElementById("choose_city").innerHTML = "Tokyo";

    
    }

    function eu(){


        //Europe London
        let latitude = '51.5002';
        let longitude = '-0.1262';
        xhttp.open("GET", `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&hourly=temperature_2m,relativehumidity_2m,rain,snowfall,cloudcover`, true);
        xhttp.send();
        console.log();

        document.getElementById("choose_city").innerHTML = "London";

    }
    
    function ca(){


        //Central America Ciudad de Mexico
        let latitude = '19.4271';
        let longitude = '-99.1276';
        xhttp.open("GET", `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&hourly=temperature_2m,relativehumidity_2m,rain,snowfall,cloudcover`, true);
        xhttp.send();
        console.log();

        document.getElementById("choose_city").innerHTML = "Ciudad de Mexico";


    }
    
    function na(){

        //North America Washington DC
        let latitude = '38.8921';
        let longitude = '-77.0241';
        xhttp.open("GET", `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&hourly=temperature_2m,relativehumidity_2m,rain,snowfall,cloudcover`, true);
        xhttp.send();
        
        document.getElementById("choose_city").innerHTML = "Washington DC";


    }

    function sa(){



        //South America Brasilia DF
        let latitude = '-47.9292';
        let longitude = '-15.7801';
        xhttp.open("GET", `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&hourly=temperature_2m,relativehumidity_2m,rain,snowfall,cloudcover`, true);
        xhttp.send();


        document.getElementById("choose_city").innerHTML = "Brasilia DF";
    }

    
    
    
    
    








//if(confirm("Click OK if you accept using the cookies for a better experience")){
//
//}
//else{
//    //location.href = "www.ifc.com"
//}
//


const btn1 = document.getElementById("btn1");
const btn2 = document.getElementById("btn2");
const btn3 = document.getElementById("btn3");


//btn1.addEventListener('click', function button1(){
//
//    if(confirm("Desejas ir para o outro site?")){
//        location.href = "www.google.com";
//    }
//    else{
//        
//    }
//
//});
//