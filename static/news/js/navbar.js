current_link = window.location.href
current_link = current_link.split('/')
console.log(current_link)


if (current_link.indexOf('#') > -1) {
    current_link.splice(current_link.indexOf('#'), 1)
}

// delete all '' from array
while (current_link.indexOf('') > -1) {
    current_link.splice(current_link.indexOf(''), 1)
}
console.log(current_link)


nav_list = $('.menu_link')
console.log(nav_list)
for (var i = 0; i < nav_list.length; i += 1) {
    if (current_link[current_link.length - 1] == nav_list[i].id) {
        nav_list[i].classList.add('activate')
    }
}

// function clicked() {
//     links = document.getElementsByClassName('menu_link');
//     for (var i = 0; i < links.length; i += 1) {
//         links[i].classList.remove('activate')
//     }
//     document.addEventListener('click', e => add_class(e));
// }

// function add_class(elem) {
//     // console.log(elem.target)
//     element = elem.target;
//     element.classList.add('activate')
// }   

// $(document).ready(function () {

//     $('.menu_link').click(function() {
//         $('.menu_link').removeCl ass('activate')
//         $(this).addClass('activate')
//     })
// })