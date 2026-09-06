function toggleInvert() {
    document.body.classList.toggle('inverted');
}
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
async function erikaButton() {
    new Audio('erika.mp3').play();
    for (let i = 0; i <= 61; i++) {
        toggleInvert();
        await sleep(50);
        
    }
}