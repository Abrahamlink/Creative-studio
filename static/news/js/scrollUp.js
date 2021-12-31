const scroll = document.querySelector('.scroll-block');

window.onscroll = () => {
    if (window.scrollY > 700) {
        scroll.classList.remove('scroll_hide');
    }

    if (window.scrollY < 500) {
        scroll.classList.add('scroll_hide');
    }
}

scroll.onclick = (e) => {
    e.preventDefault()
    $('html').animate({scrollTop: 0}, 700)
}