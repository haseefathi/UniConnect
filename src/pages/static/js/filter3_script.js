function filter_users() {

    // getting values from all filters
    let name_filter = document.getElementById('filter_user_name').value.toUpperCase().trim();
    let uni_filter = document.getElementById('accepted_uni_filter').value.toUpperCase().trim();
    let o_city_filter = document.getElementById('filter_origin_city').value.toUpperCase().trim();
    let o_country_filter = document.getElementById('filter_origin_country').value.toUpperCase().trim();
    let d_city_filter = document.getElementById('filter_dest_city').value.toUpperCase().trim();
    let d_country_filter = document.getElementById('filter_dest_country').value.toUpperCase().trim();


    if (name_filter.length == 0) {
        name_filter = null;
    }
    if (uni_filter.length == 0) {
        uni_filter = null;
    }
    if (o_city_filter.length == 0) {
        o_city_filter = null;
    }
    if (o_country_filter.length == 0) {
        o_country_filter = null;
    }
    if (d_city_filter.length == 0) {
        d_city_filter = null;
    }
    if (d_country_filter.length == 0) {
        d_country_filter = null;
    }

    console.log(name_filter);
    console.log(uni_filter);
    console.log(o_city_filter);
    console.log(o_country_filter);
    console.log(d_city_filter);
    console.log(d_country_filter);

    let name_filter_info = {
        filter: name_filter,
        container_classname: 'name_container',
        value_classname: 'name_value'
    };

    let uni_filter_info = {
        filter: uni_filter,
        container_classname: 'university_container',
        value_classname: 'university_value'
    };

    let o_city_filter_info = {
        filter: o_city_filter,
        container_classname: 'from_container',
        value_classname: 'o_city_value'
    };

    let o_country_filter_info = {
        filter: o_country_filter,
        container_classname: 'from_container',
        value_classname: 'o_country_value'
    };

    let d_city_filter_info = {
        filter: d_city_filter,
        container_classname: 'destination_container',
        value_classname: 'd_city_value'
    };

    let d_country_filter_info = {
        filter: d_country_filter,
        container_classname: 'destination_container',
        value_classname: 'd_country_value'
    };

    let filters = [name_filter_info, uni_filter_info, o_city_filter_info, o_country_filter_info, d_city_filter_info, d_country_filter_info];

    // loop through all filters
    for (let i = 0; i < filters.length; i++) {
        let visible_users = getUserVisibilities()[2];
        applyFilter(filters[i], visible_users);
    }


}

function applyFilter(filter, users) {
    for (i = 0; i < users.length; i++) {

        let container = users[i].getElementsByClassName(filter.container_classname)[0];
        let value = container.getElementsByClassName(filter.value_classname)[0];
        value = value.innerText.toUpperCase().trim();
        // console.log('value');

        // let user_details_container = visible_users[i].parentNode;
        // let user_cell_element = user_details_container.parentNode;

        let user_cell_element = users[i];

        if (filter.filter == null) {
            continue;
        }

        if (value.indexOf(filter.filter) > -1) {
            user_cell_element.style.display = "block";
        } else {
            user_cell_element.style.display = "none";
        }

    }
}

function getUserVisibilities() {
    // console.log('getting visible users');
    let all_user_divs = document.getElementsByClassName("user_cell");
    let visible_users = [];
    let hidden_users = [];
    let all_users = [];
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
        all_users.push(all_user_divs[i]);
    }
    // console.log("visible u: " + visible_users.length);
    return [visible_users, hidden_users, all_users];
}