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