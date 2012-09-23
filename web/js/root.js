$(document).ready(function() {
    $.ajax({
        url: '/python-webpy-openid-api/info',
        success: function(data) {
            $('#version').html(data.version);
            $('#version').fadeIn(2000);
        },
        error: function(data, status) {
            console.log("error " + status);
        }
    });
});

