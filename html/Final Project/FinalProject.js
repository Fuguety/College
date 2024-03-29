const xhttp = new XMLHttpRequest();
    xhttp.onload = function () {

        requestData = JSON.parse(this.responseText);
        console.log(requestData);

    }


    
    function na(){

        xhttp.onload = function () {

            requestData = JSON.parse(this.responseText);
            document.getElementById("temperature").innerHTML = "Temperature in ºC: " + requestData["current_weather"]["temperature"];
    
        }

        //North America Washington DC
        let latitude = '38.8921';
        let longitude = '-77.0241';
        xhttp.open("GET", `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&hourly=temperature_2m&current_weather=true`, true);
        xhttp.send();
        
        document.getElementById("choose_city").innerHTML = "Washington DC";
        document.getElementById("more_info").href = "./Washigton_DC.html";

    }
    
    function ca(){

        xhttp.onload = function () {

            requestData = JSON.parse(this.responseText);
            document.getElementById("temperature").innerHTML = "Temperature in ºC: " + requestData["current_weather"]["temperature"];
    
        }


        //Central America Ciudad de Mexico
        let latitude = '19.4271';
        let longitude = '-99.1276';
        xhttp.open("GET", `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&hourly=temperature_2m&current_weather=true`, true);
        xhttp.send();

        document.getElementById("choose_city").innerHTML = "Ciudad de Mexico";
        document.getElementById("more_info").href = "./Ciudad_de_Mexico.html";


    }
    
    function sa(){

        xhttp.onload = function () {

            requestData = JSON.parse(this.responseText);
            document.getElementById("temperature").innerHTML = "Temperature in ºC: " + requestData["current_weather"]["temperature"];

        }

        //South America Brasilia DF
        let latitude = '-15.7801';
        let longitude = '-47.9292';
        xhttp.open("GET", `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&hourly=temperature_2m&current_weather=true`, true);
        xhttp.send();
        
        
        document.getElementById("choose_city").innerHTML = "Brasilia DF";
        document.getElementById("more_info").href = "./Brasilia_DF.html";

        
    }

    function eu(){

        xhttp.onload = function () {

            requestData = JSON.parse(this.responseText);
            document.getElementById("temperature").innerHTML = "Temperature in ºC: " + requestData["current_weather"]["temperature"];
    
        }

        //Europe London
        let latitude = '51.5002';
        let longitude = '-0.1262';
        xhttp.open("GET", `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&hourly=temperature_2m&current_weather=true`, true);
        xhttp.send();

        document.getElementById("choose_city").innerHTML = "London";
        document.getElementById("more_info").href = "./London.html";


    }
    
    function af(){

        xhttp.onload = function () {

            requestData = JSON.parse(this.responseText);
            document.getElementById("temperature").innerHTML = "Temperature in ºC: " + requestData["current_weather"]["temperature"];
    
        }

        //Africa Nairobi
        let latitude = '-1.28';
        let longitude = '36.82';
        xhttp.open("GET", `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&hourly=temperature_2m&current_weather=true`, true);
        xhttp.send();

        document.getElementById("choose_city").innerHTML = "Nairobi";
        document.getElementById("more_info").href = "./Nairobi.html";
    }
    
    function as(){

        xhttp.onload = function () {

            requestData = JSON.parse(this.responseText);
            document.getElementById("temperature").innerHTML = "Temperature in ºC: " + requestData["current_weather"]["temperature"];
    
        }

        //Asia Tokyo

        let latitude = '35.6785';
        let longitude = '139.6823';
        xhttp.open("GET", `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&hourly=temperature_2m&current_weather=true`, true);
        xhttp.send();

        document.getElementById("choose_city").innerHTML = "Tokyo";
        document.getElementById("more_info").href = "./Tokyo.html";

    
    }

    function oc(){

        xhttp.onload = function () {

            requestData = JSON.parse(this.responseText);
            document.getElementById("temperature").innerHTML = "Temperature in ºC: " + requestData["current_weather"]["temperature"];
    
        }
        //Oceanic Canberra

        let latitude = '-35.2820';
        let longitude = '149.1286';
        xhttp.open("GET", `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&hourly=temperature_2m&current_weather=true`, true);
        xhttp.send();
        
        
        document.getElementById("choose_city").innerHTML = "Canberra";
        document.getElementById("more_info").href = "./Canberra.html";

    }

    




    
    
