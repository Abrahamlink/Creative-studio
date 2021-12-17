$(document).ready(function() {
    $('.burger').click(function(event) {
        $('.burger, .navbar__block').toggleClass('active');
        $('body').toggleClass('no_scroll');
    })
});