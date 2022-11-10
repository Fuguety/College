const xhttp = new XMLHttpRequest();
    xhttp.onload = function () {

        requestData = JSON.parse(this.responseText);
        console.log(requestData);

    }


    const africa = document.getElementById("af");
    const asia = document.getElementById("asia");
    const oc = document.getElementById("oc");
    const eu = document.getElementById("eu");
    const na = document.getElementById("na");
    const ca = document.getElementById("ca");
    const sa = document.getElementById("sa");
    


    africa.addEventListener('click',function africa(){

        //Africa
        let longitude = '-47.9292';
        let latitude = '-15.7801';
        xhttp.open("GET", `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&hourly=temperature_2m,relativehumidity_2m,rain,snowfall,cloudcover`, true);
        xhttp.send();


    })


    oc.addEventListener('click',function oc(){

        //OC
        let longitude = '-47.9292';
        let latitude = '-15.7801';
        xhttp.open("GET", `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&hourly=temperature_2m,relativehumidity_2m,rain,snowfall,cloudcover`, true);
        xhttp.send();

    })

    asia.addEventListener('click',function asia(){

        //Asia
        let longitude = '-47.9292';
        let latitude = '-15.7801';
        xhttp.open("GET", `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&hourly=temperature_2m,relativehumidity_2m,rain,snowfall,cloudcover`, true);
        xhttp.send();

    
    })
    
    
    eu.addEventListener('click',function eu(){

        //EU
        let longitude = '-47.9292';
        let latitude = '-15.7801';
        xhttp.open("GET", `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&hourly=temperature_2m,relativehumidity_2m,rain,snowfall,cloudcover`, true);
        xhttp.send();

    })


    ca.addEventListener('click',function ca(){

        //CA
        let longitude = '-47.9292';
        let latitude = '-15.7801';
        xhttp.open("GET", `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&hourly=temperature_2m,relativehumidity_2m,rain,snowfall,cloudcover`, true);
        xhttp.send();

    })

    na.addEventListener('click',function na(){

        //NA
        let longitude = '-47.9292';
        let latitude = '-15.7801';
        xhttp.open("GET", `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&hourly=temperature_2m,relativehumidity_2m,rain,snowfall,cloudcover`, true);
        xhttp.send();

    })

    function sa(){

        //brasilia SA
        //let longitude = '-47.9292';
        //let latitude = '-15.7801';
        //xhttp.open("GET", `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&hourly=temperature_2m,relativehumidity_2m,rain,snowfall,cloudcover`, true);
        //xhttp.send();
        //
        document.getElementById("sa").innerHTML = "oiiii";
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


