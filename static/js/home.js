let listIcon = document.querySelector('.icon-list');
listIcon.addEventListener('click', function(event){
    let slideDiv = document.querySelector('.slideDiv');
    slideDiv.classList.toggle('slideClose');
    slideDiv.classList.remove('slideCloseMotion');
    slideDiv.classList.add('slideOpenMotion');
});

let slideCloseIcon = document.querySelector('.icon-slideClose');
slideCloseIcon.addEventListener('click', function(event){
    let slideDiv = document.querySelector('.slideDiv');
    slideDiv.classList.toggle('slideClose');
    slideDiv.classList.remove('slideOpenMotion');
    slideDiv.classList.add('slideCloseMotion');
});

let dropIcon = document.querySelector('.icon-human');
let dropMenu = document.querySelector('.human-info');
let isOpen =false;
dropIcon.addEventListener('click', function(event){
    let target = document.querySelector('.hidden-nav-bar');
    let duration = 200;

    if(!isOpen) {
        target.style.display = 'block';
        let height = target.offsetHeight;
        target.childNodes[1].style.display = 'none';
        target.style.height = '0';
        target.offsetHeight;
        target.style.transitionProperty = "height";
        target.style.transitionDuration = duration + 'ms';
        target.style.height = height + 'px';
        window.setTimeout(() => {
            target.style.removeProperty('height');
            target.style.removeProperty('transition-duration');
            target.style.removeProperty('transition-property');
            target.childNodes[1].style.display = 'block';
            isOpen=true;
        }, duration);
    }
    else {
        target.style.height = target.offsetHeight + 'px';
        target.childNodes[1].style.display = 'none';
        target.style.transitionProperty = "height";
        target.style.transitionDuration = duration + 'ms';
        target.offsetHeight;
        target.style.height = '0';
        window.setTimeout(() => {
            target.style.removeProperty('height');
            target.style.removeProperty('transition-duration');
            target.style.removeProperty('transition-property');
            target.style.display = 'none';
            target.childNodes[1].style.display = 'block';
            isOpen=false;
        }, duration);
    }
});