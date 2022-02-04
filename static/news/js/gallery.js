function GalleryFiller() {
    const gallery_block = $('#gallery_all_images')

    $('#tag_select').change(() => {
        let selected_url  = '/news' + $("#tag_select option:selected").val()
        let selected_text = $("#tag_select option:selected").html()

        // Make empty space in block
        gallery_block.empty()

        $.getJSON(selected_url, (data) => {
            $.each(data, (i, val) => {
                let path = '/media/' + val.image
                let layout = '<div class="image"><a href="'+ path +'" data-fancybox="gallery" class="image_link"><img src="'+ path +'" alt="" class="gallery-image"></a></div>'

                gallery_block.append(layout)
            })
        })
    })
}

GalleryFiller()


// $(document).ready(function() {
//     image = document.getElementById('main-image')
//     h = image.naturalHeight
//     w = image.naturalWidth
//     console.log(`${w}x${h}`)
// });

// function CheckSizesOfImages() {
//     let images = $('.gallery-image')
//     console.log(images)
// }

// CheckSizesOfImages()

// $('#tag_select').change(() => {
//     link = document.getElementsByClassName('image_link')
//     console.log(link)
//     lin = $('a.image_link')
//     console.log(lin)
//     console.log(lin.children('img.gallery_image'))
// })

// $('#tag_select').change(() => {
//     $('a.image_link').each(function() {
//         console.log($(this))
//     })
// })
