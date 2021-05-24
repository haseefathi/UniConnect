function showModal(profile_public) {
    // Get the modal
    var modal = document.getElementById("toggle_modal");
    var modal_body = document.getElementsByClassName("modal-body")[0];
    var modal_heading_status = document.getElementById("profile_status");
    let notification = document.getElementsByClassName("profile_public_notification")[0];

    console.log(notification.innerHTML);

    // Get the cancel button
    var cancel = document.getElementById("confirm_button");

    // When the user clicks the button, open the modal 

    modal.style.display = "block";
    if (profile_public) {
        modal_body.innerHTML = "<p>Your profile is currently public and can be seen by others. This allows people to find you.</p>";
        modal_heading_status.innerHTML = "Public";
        notification.innerHTML = "<p>Your profile is public and can be seen by others.</p>";
    } else {
        modal_body.innerHTML = "<p>Your profile is private and is not visible to others. This prevents people from finding you.</p>";
        modal_heading_status.innerHTML = "Private";
        notification.innerHTML = "<p> Your profile is private and is not visible to others.</p>";
    }

    // When the user clicks on <span> (x), close the modal
    cancel.onclick = function() {
        modal.style.display = "none";
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
    // console.log('toggle switch value: ' + toggle_switch.checked);
    let csrf_value = getCookie('csrftoken');
    let profile_public = false;
    if (toggle_switch.checked) {
        profile_public = true;
    }

    $.post("/user/change_profile_status/", {
        is_public: profile_public,
        csrfmiddlewaretoken: csrf_value
    });

    //changing the notification at the bottom

    showModal(profile_public);


}