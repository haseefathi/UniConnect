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


function accept_friend_request(request_id, username) {
    let accept_url = '/user/accept_friend_request/';
    let csrf_value = getCookie('csrftoken');
    console.log('in fn 1 ' + username);

    //accepting the request
    $.post(accept_url, {
        request_id: request_id,
        csrfmiddlewaretoken: csrf_value
    });

    add_friend_to_list(request_id, username);
    remove_element(request_id);


}


function send_friend_request(to_username) {
    let send_url = '/user/send_friend_request/';
    let csrf_value = getCookie('csrftoken');

    console.log('sending the request');
    //sending the request the request
    $.post(send_url, {
        to_username: to_username,
        csrfmiddlewaretoken: csrf_value
    });

    // disable button once sent
    console.log('disabling button');
    let send_button = document.getElementById("send_request_button");
    send_button.classList.add("disabled");
    send_button.innerHTML = `<i class="fas fa-check-circle"></i> Request has been sent! `;
    send_button.disabled = 'true';
    send_button.style.backgroundColor = '#808080';
    send_button.style.color = '#fff';


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


function add_friend_to_list(request_id, username) {

    let no_friends_message = document.getElementById('no_friends_message');
    console.log('changing display of message');
    if (no_friends_message) {
        no_friends_message.style.display = "none";
    }

    let container_id = `container_request_${request_id}`;
    let user_container = document.getElementById(container_id);
    let friend_name = user_container.getElementsByClassName('name_value')[0].innerText;

    let img_element_container = user_container.getElementsByClassName('picture_container')[0];
    let img_element = img_element_container.getElementsByClassName('profile_picture')[0];
    let img_src = img_element.src;

    // console.log(img_src);
    // console.log(username);
    // console.log(friend_name);

    // creating a new friend element
    var new_friend_box = document.createElement("div");
    new_friend_box.className = 'friend_box';
    new_friend_box.innerHTML = `
        <div class="three_columns">
            <div class="profile_picture_container">
                <img src="${img_src}" alt="profile_pic" class="profile_picture"> 
            </div>
            <div class="name_container">
                <p>${friend_name}</p>
            </div>
            <div class="button_container">
                <button onclick="open_chat('${username}')"><i class="fas fa-comment"></i></button>
            </div>
        </div>
    `;

    // appending it to the friends list
    var friends_div = document.getElementsByClassName('friends_div')[0];
    friends_div.appendChild(new_friend_box);
}



function search_friends() {
    console.log('searching');
    var input, container_classname, value_classname, filter, i;

    input = document.getElementById('search_friend_input');
    value_classname = 'name_container';

    filter = input.value.toUpperCase().trim();
    let all_friends = document.getElementsByClassName("friend_box");

    for (i = 0; i < all_friends.length; i++) {

        let value = all_friends[i].getElementsByClassName(value_classname)[0];
        value = value.innerText.toUpperCase().trim();
        console.log('value ' + value);

        let user_cell_element = all_friends[i];

        if (value.indexOf(filter) > -1) {
            user_cell_element.style.display = "block";
        } else {
            user_cell_element.style.display = "none";
        }

    }
}