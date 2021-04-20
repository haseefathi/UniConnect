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

function showForm() {
    showLoadingSign();
    clearNavbarHighlight();
    document.getElementById("nav-universities").classList.add("active");
    $.ajax({
        url: '/user/update-grad-adm-profile',
        type: 'GET',
        dataType: 'html',
        data: {
            // 'csrfmiddlewaretoken': getCookie('csrftoken'),
            //'initialrender': true,
        },
        success: function(content) {
            closeLoadingSign();
            $('#mainContent').html(content);
            scrollToTop();

        },
        failure: function() {
            alert('Something wrong with the server bro...');
        }
    });
}


function universitySearch() {
    var college_name = document.getElementById("university-search-input").value;

    // only do if a college name has been entered 
    if (college_name.length != 0 || college_name !== "" || college_name.replace(/\s+/g, '').length != 0) {
        showLoadingSign();
        clearNavbarHighlight();
        document.getElementById("nav-universities").classList.add("active");
        $.ajax({
            url: '/user/university-search/',
            type: 'GET',
            dataType: 'html',
            data: {
                // 'csrfmiddlewaretoken': getCookie('csrftoken'),
                //'initialrender': true,
                'college_name': college_name
            },
            success: function(content) {
                closeLoadingSign();
                $('#mainContent').html(content);
                scrollToTop();
            },
            failure: function() {
                alert('Something wrong with the server bro...');
            }
        });
    }
}