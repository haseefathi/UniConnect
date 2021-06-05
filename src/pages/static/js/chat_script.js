function open_chat(username) {
    // alert('opening chat of: ' + username);

    showLoadingSign();
    clearNavbarHighlight();
    document.getElementById("nav-requests").classList.add("active");
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var response = this.responseText;
            closeLoadingSign();
            $('#mainContent').html(response);
            // document.getElementById("mainContent").innerHTML = response;
        }
    };
    scrollToTop();

    let chat_url = `/user/chat/dialogs/${username}`;

    xhttp.open("GET", chat_url, true);
    xhttp.send();
}