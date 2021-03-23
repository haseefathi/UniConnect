function showUnis() {
    alert('clicked');
}


function showDashboard(event) {
    clearNavbarHighlight();
    event.classList.add("active");
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("mainContent").innerHTML = this.responseText;
        }
    };
    xhttp.open("GET", "/dashboard", true);
    xhttp.send();
}

function showPredictor(event) {
    clearNavbarHighlight();
    event.classList.add("active");
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("mainContent").innerHTML = this.responseText;
        }
    };
    xhttp.open("GET", "/predictor", true);
    xhttp.send();
}


function showUniversities(event) {
    clearNavbarHighlight();
    event.classList.add("active");
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("mainContent").innerHTML = this.responseText;
        }
    };
    xhttp.open("GET", "/universities", true);
    xhttp.send();
}

function clearNavbarHighlight() {
    var navList = document.getElementById('navList').getElementsByTagName("li");
    var msg = "";
    for (let i = 0; i < navList.length; i++) {
        let innerLinkTag = navList[i].getElementsByTagName("a")[0];
        innerLinkTag.classList.remove("active");
    }
}