var apiBase = "/backbone-webpy-openid-api/";

$(document).ready(function() {
    $.ajax({
        url: apiBase + "info",
        success: function(data) {
            $('#version').html(data.version);
            $('#version').fadeIn(2000);
        },
        error: function(data, status) {
            console.log("error " + status);
        }
    });

    $.ajax({
        url: apiBase + "user",
        success: function() { $("#enter").fadeIn(2000); },
        statusCode: {
            401: function() { $("#sign-in").fadeIn(2000); }
        }
    });
});

