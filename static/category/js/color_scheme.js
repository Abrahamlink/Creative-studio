color_blocks = $('.color p')
for (i = 0; i != color_blocks.length; i++) {
    color = color_blocks[i].textContent
    block = color_blocks[i].parentNode
    if (color == 'green') {
        block.style.background = color
    } else {
        block.style.background = `#${color}`
    }
}


font_exemples = $('.font-example')
font_names = $('.font-name span')
for (i = 0; i != font_names.length; i++) {
    console.log(font_names[i].textContent);
    $(font_exemples[i]).css("font-family", font_names[i].textContent)
}

$('.pleasure').click(function() {
    $.ajax({
        url: 'studio',
        type: 'get',
        data: {
            button_text: $(this).text()
        },
        success: function(response) {
            console.log('haeu')
        }
    })
})
