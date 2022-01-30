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
        console.log(current_link)
        current_link = current_link.replace('/', replace_data['/'])
        current_link = current_link.replace(':', replace_data[':'])
    }
    if (i >= current_link.length) {
        run = false
    }
}
console.log(current_link)

$(document).ready(function() {
    links = $('.social_networks a');
    console.log(links.length)
    for (i = 0; i < links.length; i++) {
        link = links[i].href
        console.log(link)
        there = link.indexOf('$LINK$')
        if (there != -1) {
            link_r = link.replace('$LINK$', current_link)
            links[i].href = link_r
        }
    }
});

