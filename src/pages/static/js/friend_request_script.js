function delete_friend_request(request_id) {

    let delete_url = '/user/delete_friend_request/';
    let csrf_value = getCookie('csrftoken');

    //deleting the request from DB
    $.post(delete_url, {
        request_id: request_id,
        csrfmiddlewaretoken: csrf_value
    });

    //removing the request from front end
    remove_element(request_id);

}


function accept_friend_request(request_id) {
    let accept_url = '/user/accept_friend_request/';
    let csrf_value = getCookie('csrftoken');

    //accepting the request
    $.post(accept_url, {
        request_id: request_id,
        csrfmiddlewaretoken: csrf_value
    });

    remove_element(request_id);

}


function send_friend_request(to_username) {
    let send_url = '/user/send_friend_request/';
    let csrf_value = getCookie('csrftoken');

    console.log('sending the request')
        //sending the request the request
    $.post(send_url, {
        to_username: to_username,
        csrfmiddlewaretoken: csrf_value
    });
}


function remove_element(request_id) {
    let container_id = `container_request_${request_id}`;
    let user_container = document.getElementById(container_id);
    user_container.remove();

    let remaining_requests = document.getElementsByClassName("user_cell");
    if (remaining_requests.length == 0) {
        let message = document.getElementById('request_message');
        message.innerText = "You have no pending requests.";
    }
}