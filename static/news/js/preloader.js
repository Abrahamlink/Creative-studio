window.onload = function() {
    let preloader = document.getElementById('preloader');
    preloader.classList.add('disabled')
    sleep(250);
    preloader.style.visibility = 'hidden'
};

function sleep(milliseconds) {
    const date = Date.now();
    let currentDate = null;
    do {
      currentDate = Date.now();
    } while (currentDate - date < milliseconds);
}


// function sleep(ms) {
//     return new Promise(resolve => setTimeout(resolve, ms));
//   }