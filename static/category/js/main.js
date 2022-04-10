$(document).on('click', function(event) {
    try {
        cls = event.target.className.split(' ')
        if ((cls.indexOf('activator') != -1 ) || (cls.indexOf('close') != -1)) {
            cls = event.target.getAttribute('data')
            block = $('#'+cls)
            block.fadeToggle(200)
        }
    }
    catch {
        console.log('some error')
    }
})

$(document).ready(function() {
    try {
        image = document.getElementById('main-image')
        h = image.naturalHeight
        w = image.naturalWidth
    } catch {
        console.log('error')
    }
});


// function popup() {
//     cls = button.attr("href")
//     let block = $(cls)
//     if (block.attr('hidden') != "hidden") {
//         block.attr('hidden', true)
//     } else {
//         block.removeAttr('hidden')
//     }
// }


// button.onclick = popup;