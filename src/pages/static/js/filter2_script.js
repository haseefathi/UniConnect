function filter_users(key) {
    console.log('new file yo');
    var input, container_classname, value_classname, filter, i;

    var checkbox = false;

    if (key == 'name') {
        input = document.getElementById("filter_user_name");
        container_classname = "name_container";
        value_classname = "name_value";
    } else if (key == 'uni') {
        input = document.getElementById("accepted_uni_filter");
        container_classname = "university_container";
        value_classname = "university_value";
    } else if (key == 'o_city') {
        input = document.getElementById("filter_origin_city");
        container_classname = "from_container";
        value_classname = "o_city_value";
    } else if (key == 'o_country') {
        input = document.getElementById("filter_origin_country");
        container_classname = "from_container";
        value_classname = "o_country_value";
    } else if (key == 'd_city') {
        input = document.getElementById("filter_dest_city");
        container_classname = "destination_container";
        value_classname = "d_city_value";
    } else if (key == 'd_country') {
        input = document.getElementById("filter_dest_country");
        container_classname = "destination_container";
        value_classname = "d_country_value";
    } else if (key == 'f_gender') {
        input = document.getElementById("female_checkbox");
        container_classname = "picture_container";
        value_classname = "gender_value";
        checkbox = true;
    } else if (key == 'm_gender') {
        input = document.getElementById("male_checkbox");
        container_classname = "picture_container";
        value_classname = "gender_value";
        checkbox = true;
    }


    if (!checkbox) {
        filter = input.value.toUpperCase().trim();

        let user_visibilities = getUserVisibilities();
        let visible_users = user_visibilities[0];
        let hidden_users = user_visibilities[1];

        console.log('currently visible: ' + visible_users.length);
        console.log('currently hidden: ' + hidden_users.length);

        // remove from currently visible users
        for (i = 0; i < visible_users.length; i++) {

            let container = visible_users[i].getElementsByClassName(container_classname)[0];
            let value = container.getElementsByClassName(value_classname)[0];
            value = value.innerText.toUpperCase().trim();
            console.log('value');

            // let user_details_container = visible_users[i].parentNode;
            // let user_cell_element = user_details_container.parentNode;

            let user_cell_element = visible_users[i];

            if (value.indexOf(filter) > -1) {
                user_cell_element.style.display = "block";
            } else {
                user_cell_element.style.display = "none";
            }

        }

        // filter from hidden users
        for (i = 0; i < hidden_users.length; i++) {
            let container = hidden_users[i].getElementsByClassName(container_classname)[0];
            let value = container.getElementsByClassName(value_classname)[0];
            value = value.innerText.toUpperCase().trim();
            console.log('value');

            // let user_details_container = visible_users[i].parentNode;
            // let user_cell_element = user_details_container.parentNode;

            let user_cell_element = hidden_users[i];

            if (value.indexOf(filter) > -1) {
                user_cell_element.style.display = "block";
            } else {
                user_cell_element.style.display = "none";
            }


        }

    } else {

        let checked = input.checked;
        let filter = input.value;

        let all_user_divs = document.getElementsByClassName("user_details_list_container");

        for (i = 0; i < all_user_divs.length; i++) {

            let container = all_user_divs[i].getElementsByClassName(container_classname)[0];
            let value = container.getElementsByClassName(value_classname)[0];
            value = value.innerText.toUpperCase().trim();

            let user_details_container = all_user_divs[i].parentNode;
            let user_cell_element = user_details_container.parentNode;

            if ((value == filter) && checked) {
                user_cell_element.style.display = "block";
            } else if ((value == filter) && !checked) {
                user_cell_element.style.display = "none";
            }

        }


    }


}


function getUserVisibilities() {
    // console.log('getting visible users');
    let all_user_divs = document.getElementsByClassName("user_cell");
    let visible_users = [];
    let hidden_users = [];
    // console.log(all_user_divs[0].getElementsByClassName('name_value')[0].innerText);
    // console.log(all_user_divs[0].);

    for (let i = 0; i < all_user_divs.length; i++) {
        if (window.getComputedStyle(all_user_divs[i]).display === "none") {
            console.log(all_user_divs[i].getElementsByClassName('name_value')[0].innerText + " is hidden");
            hidden_users.push(all_user_divs[i]);
        } else {
            console.log(all_user_divs[i].getElementsByClassName('name_value')[0].innerText + " is visible");
            visible_users.push(all_user_divs[i]);
        }
    }
    // console.log("visible u: " + visible_users.length);
    return [visible_users, hidden_users];
}