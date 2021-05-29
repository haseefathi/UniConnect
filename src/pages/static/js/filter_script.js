function filter_users(key) {

    var input, container_classname, value_classname, filter, i;

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
    }

    filter = input.value.toUpperCase().trim();

    outer_list_container = document.getElementById("outer_user_container");
    all_user_divs = document.getElementsByClassName("user_details_list_container");

    for (i = 0; i < all_user_divs.length; i++) {

        let container = all_user_divs[i].getElementsByClassName(container_classname)[0];
        let value = container.getElementsByClassName(value_classname)[0];
        value = value.innerText.toUpperCase().trim();

        let user_details_container = all_user_divs[i].parentNode;
        let user_cell_element = user_details_container.parentNode;

        if (value.indexOf(filter) > -1) {
            user_cell_element.style.display = "";
        } else {
            user_cell_element.style.display = "none";
        }

    }
}