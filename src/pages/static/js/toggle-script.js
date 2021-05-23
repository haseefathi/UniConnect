function showModal(profile_public) {
    // Get the modal
    var modal = document.getElementById("toggle_modal");

    // Get the cancel button
    var cancel = document.getElementById("confirm_button");

    // When the user clicks the button, open the modal 

    modal.style.display = "block";

    // When the user clicks on <span> (x), close the modal
    cancel.onclick = function() {
        modal.style.display = "none";
        showProfile();
    }
}

// function to get csrf token cookie value 
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}




function change_profile_status(toggle_switch) {
    console.log('toggle switch value: ' + toggle_switch.checked);
    let csrf_value = getCookie('csrftoken');
    let profile_public = false;
    if (toggle_switch.checked) {
        profile_public = true;
    }

    console.log('csrf_value: ' + csrf_value);
    console.log('toggle value: ' + profile_public);

    $.post("/user/change_profile_status/", {
        is_public: profile_public,
        csrfmiddlewaretoken: csrf_value
    });
    showModal(profile_public);


}