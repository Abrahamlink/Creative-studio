current_link = window.location.href

replace_data = {
    '/': '%2F',
    ':': '%3A',
}

run = true
i = 0
while (run) {
    i++
    if (current_link.indexOf('/') != -1 || current_link.indexOf(':') != -1) {
        current_link = current_link.replace('/', replace_data['/'])
        current_link = current_link.replace(':', replace_data[':'])
    }
    if (i >= current_link.length) {
        run = false
    }
}

$(document).ready(function() {
    links = $('.social_networks a');
    for (i = 0; i < links.length; i++) {
        link = links[i].href
        there = link.indexOf('$LINK$')
        if (there != -1) {
            link_r = link.replace('$LINK$', current_link)
            links[i].href = link_r
        }
    }
});

button_load = '<a id="more-comment-loader">Загрузить еще...</a>'
comments_count = $('#all-comments-count').html()
cur_comments_count = $('.comment-container').length
url = window.location.href;
if (Number(comments_count) > cur_comments_count) {
    $('.comments_wrapper').append(button_load)
}

$('#more-comment-loader').click(function() {
    let local_cur_comments_count = $('.comment-container').length
    normal_url = url.substring(0, url.length - 1) + '$' + String(local_cur_comments_count);

    cur_coms = $('.comment-container').length
    $.getJSON(normal_url, (data) => {
        $.each(data, (i, val) => {
            let layout = '<div class="comment-container alert alert-warning hide"><p class="author">' + val.author.substring(0, 16) + '</p><div class="text">' + val.text + '</div><p class="date">' + val.pubdate + '</p></div>'
            $('.comments_wrapper').append(layout);
        });
        containers = $('.comment-container')
        for (i=cur_coms; i <= containers.length - 1; i++) {
            // $('.comment-container')[i].removeClass('hide')
            $('.comment-container')[i].classList.remove('hide')
        }
        $('#more-comment-loader').insertAfter(containers[containers.length - 1])
        console.log(Number(comments_count), $('.comment-container').length)
        if (Number(comments_count) == $('.comment-container').length) {
            $('#more-comment-loader').remove()
        }
    });
});

function sleep(milliseconds) {
    const date = Date.now();
    let currentDate = null;
    do {
      currentDate = Date.now();
    } while (currentDate - date < milliseconds);
}