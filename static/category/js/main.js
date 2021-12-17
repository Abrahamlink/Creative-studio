$(document).on('click', function(event) {
    try {
        cls = event.target.className.split(' ')
        if ((cls.indexOf('activator') != -1 ) || (cls.indexOf('close') != -1)) {
            cls = event.target.getAttribute('data')
            block = $('#'+cls)
            block.fadeToggle(300)
        }
    }
    catch {
        console.log('noob')
    }
})


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