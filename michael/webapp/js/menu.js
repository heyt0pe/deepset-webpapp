let menuOpened = false;

function toggleMenu() {
    let menu = document.getElementById('menu');
    menuOpened = !menuOpened
    if (menuOpened) {
        menu.style.display = 'flex';
    } else {
        menu.style.display = 'none';
    }
}