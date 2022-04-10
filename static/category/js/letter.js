$(document).ready(function() {
    pass_input = $("input[name='password']");

    par = pass_input.parent();

    layout = '<div class="password_viewer" title="Посмотреть пароль"><i class="fas fa-eye"></i></div>';
    par.append(layout)
    par.css("position", "relative")
    par.addClass('password')
});

$('body').on('click', '.password_viewer', function() {
    pass_input = $("input[name='password']");

    if (pass_input.attr('type') == 'password') {
        console.log('true')
        $("input[name='password']").attr('type', 'text');
    } else {
        console.log('false')
        $("input[name='password']").attr('type', 'password');
    }
    return false;
});

$('body').on('click', '.button_cleaner', function() {
    pass_input = $("input[name='password']");
    if (pass_input.attr('type') == 'text') {
        $("input[name='password']").attr('type', 'password');
    }
});

// data = document.getElementsByClassName('comment-container');
// for (i of data) {
//     i.style.background = '#153f77'
// }