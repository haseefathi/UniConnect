function filter_users(key) {

    console.log('filtering og');

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

        let all_user_divs = document.getElementsByClassName("user_cell");

        for (i = 0; i < all_user_divs.length; i++) {

            let container = all_user_divs[i].getElementsByClassName(container_classname)[0];
            let value = container.getElementsByClassName(value_classname)[0];
            value = value.innerText.toUpperCase().trim();
            console.log('value');

            let user_cell_element = all_user_divs[i];

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