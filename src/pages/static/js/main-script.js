window.onload = function() {
    if (sessionStorage.getItem("current-page") === null) {
        showDashboard();
    } else {
        let openedPage = sessionStorage.getItem("currentPage");
        if (openedPage == "dashboard") {
            showDashboard();
        } else if (openedPage == "predictor") {
            showPredictor();
        } else if (openedPage == "universities") {
            showUniversities();
        } else if (openedPage == "research") {
            showResearch();
        } else if (openedPage == "link1") {
            showLink1();
        }
    }
};

function showDashboard() {
    clearNavbarHighlight();
    document.getElementById("nav-dashboard").classList.add("active");
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("mainContent").innerHTML = this.responseText;
        }
    };
    xhttp.open("GET", "/dashboard", true);
    xhttp.send();
    sessionStorage.setItem("current-page", "dashboard");
    console.log(sessionStorage.getItem("current-page"));
}

function showPredictor(event) {
    clearNavbarHighlight();
    document.getElementById("nav-predict").classList.add("active");
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("mainContent").innerHTML = this.responseText;
        }
    };
    xhttp.open("GET", "/predictor", true);
    xhttp.send();
    sessionStorage.setItem("current-page", "predictor");
    console.log(sessionStorage.getItem("current-page"));
}


function showUniversities(event) {
    clearNavbarHighlight();
    document.getElementById("nav-universities").classList.add("active");
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("mainContent").innerHTML = this.responseText;
        }
    };
    xhttp.open("GET", "/universities", true);
    xhttp.send();
    sessionStorage.setItem("current-page", "universities");
    console.log(sessionStorage.getItem("current-page"));
}

function showResearch(event) {
    clearNavbarHighlight();
    document.getElementById("nav-research").classList.add("active");
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("mainContent").innerHTML = this.responseText;
        }
    };
    xhttp.open("GET", "/research", true);
    xhttp.send();
    sessionStorage.setItem("current-page", "research");
    console.log(sessionStorage.getItem("current-page"));
}

function showLink1(event) {
    clearNavbarHighlight();
    document.getElementById("nav-link1").classList.add("active");
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("mainContent").innerHTML = this.responseText;
        }
    };
    xhttp.open("GET", "/link1", true);
    xhttp.send();
    sessionStorage.setItem("current-page", "link1");
    console.log(sessionStorage.getItem("current-page"));
}

function clearNavbarHighlight() {
    var navList = document.getElementById('navList').getElementsByTagName("li");
    var msg = "";
    for (let i = 0; i < navList.length; i++) {
        let innerLinkTag = navList[i].getElementsByTagName("a")[0];
        innerLinkTag.classList.remove("active");
    }
}