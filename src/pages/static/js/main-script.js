window.onload = function() {
    showDashboard();
};

function showDashboard() {
    showLoadingSign();
    clearNavbarHighlight();
    document.getElementById("nav-dashboard").classList.add("active");
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var response = this.responseText;
            closeLoadingSign();
            document.getElementById("mainContent").innerHTML = response;
        }
    };
    xhttp.open("GET", "/dashboard", true);
    xhttp.send();
}

function showPredictor(event) {
    showLoadingSign();
    clearNavbarHighlight();
    document.getElementById("nav-predict").classList.add("active");
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var response = this.responseText;
            closeLoadingSign();
            document.getElementById("mainContent").innerHTML = response;
        }
    };
    xhttp.open("GET", "/predictor", true);
    xhttp.send();
}


function showUniversities(event) {
    showLoadingSign();
    clearNavbarHighlight();
    document.getElementById("nav-universities").classList.add("active");
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var response = this.responseText;
            closeLoadingSign();
            document.getElementById("mainContent").innerHTML = response;


        }
    };
    xhttp.open("GET", "/universities", true);
    xhttp.send();
}

function showResearch(event) {
    showLoadingSign();
    clearNavbarHighlight();
    document.getElementById("nav-research").classList.add("active");
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var response = this.responseText;
            closeLoadingSign();
            document.getElementById("mainContent").innerHTML = response;
        }
    };
    xhttp.open("GET", "/research", true);
    xhttp.send();
}

function showProfile(event) {
    showLoadingSign();
    clearNavbarHighlight();
    document.getElementById("nav-profile").classList.add("active");
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var response = this.responseText;
            closeLoadingSign();
            document.getElementById("mainContent").innerHTML = response;
        }
    };
    xhttp.open("GET", "/profile", true);
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

function showLoadingSign() {
    document.getElementById('loading-sign').style.display = 'block';
    document.getElementById("mainContent").innerHTML = "";
}

function closeLoadingSign() {
    document.getElementById('loading-sign').style.display = 'none';
}